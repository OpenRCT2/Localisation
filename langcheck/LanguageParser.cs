using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using langcheck.Extensions;

namespace langcheck
{
    internal class LanguageParser
    {
        private readonly IErrorLogger _logger;
        private readonly HashSet<string> _objects = new HashSet<string>();
        private readonly HashSet<string> _scenarios = new HashSet<string>();

        private LanguageEntryType _currentEntryType;
        private readonly HashSet<string> _groupItemIdentifiers = new HashSet<string>();

        private readonly string[] ObjectOverrideIdentifiers = new[] { "NAME", "DESC", "CPTY" };
        private readonly string[] ScenarioOverrideIdentifiers = new[] { "SCNR", "PARK", "DTLS" };

        public LanguageParser(IErrorLogger logger)
        {
            _logger = logger;
        }

        public LanguageEntry ParseLine(int lineNumber, string line)
        {
            var reader = new StringReader(line);

            ParseWhitespace(reader, lineNumber, 0);

            char c;
            if (reader.TryPeek(out c))
            {
                switch (c) {
                case '#':
                    return null;
                case '[':
                    ParseGroupObject(reader, lineNumber);
                    return null;
                case '<':
                    ParseGroupScenario(reader, lineNumber);
                    return null;
                default:
                    ParseEntry(reader, lineNumber);
                    return null;
                }
            }
            return null;
        }

        private void ParseEntry(TextReader reader, int lineNumber)
        {
            if (!reader.TryReadExpected("STR_"))
            {
                _logger.LogError(lineNumber, "Expected line to start with 'STR_'");
                return;
            }

            string identifier = reader.ReadString(4);
            string[] validIdentifiers = null;

            switch (_currentEntryType) {
            case LanguageEntryType.ObjectOverride:
                validIdentifiers = ObjectOverrideIdentifiers;
                break;
            case LanguageEntryType.ScenarioOverride:
                validIdentifiers = ScenarioOverrideIdentifiers;
                break;
            }

            if (validIdentifiers == null)
            {
                ushort index;
                if (!UInt16.TryParse(identifier, out index))
                {
                    _logger.LogError(lineNumber, $"String identifier must be between {UInt16.MinValue} and {UInt16.MaxValue}");
                    return;
                }
            }
            else
            {
                if (!validIdentifiers.Contains(identifier))
                {
                    _logger.LogError(lineNumber, $"Invalid identifier '{identifier}'");
                }
                if (!_groupItemIdentifiers.Add(identifier))
                {
                    _logger.LogWarning(lineNumber, $"Entry '{identifier}' already set.");
                }
            }

            ParseWhitespace(reader, lineNumber, 4);

            if (!reader.TryReadExpected(":"))
            {
                _logger.LogError(lineNumber, "Expected ':' after identifier");
            }

            string text = reader.ReadToEnd();
        }

        private void ParseGroupObject(TextReader reader, int lineNumber)
        {
            string groupName = ParseGroup(reader, lineNumber, '[', ']');
            if (groupName == null)
            {
                return;
            }

            _currentEntryType = LanguageEntryType.ObjectOverride;
            _groupItemIdentifiers.Clear();
        }

        private void ParseGroupScenario(TextReader reader, int lineNumber)
        {
            string groupName = ParseGroup(reader, lineNumber, '<', '>');
            if (groupName == null)
            {
                return;
            }

            _currentEntryType = LanguageEntryType.ScenarioOverride;
            _groupItemIdentifiers.Clear();
        }

        private string ParseGroup(TextReader reader, int lineNumber, char openCharacter, char closeCharacter)
        {
            if (!reader.TryReadExpected(openCharacter.ToString()))
            {
                _logger.LogError(lineNumber, $"Expected '{openCharacter}'");
                return null;
            }

            var sb = new StringBuilder();
            char c;
            bool missingEndBracket = true;
            while (reader.TryRead(out c))
            {
                if (c == closeCharacter)
                {
                    missingEndBracket = false;
                    break;
                }
                else
                {
                    sb.Append(c);
                }
            }

            if (missingEndBracket)
            {
                _logger.LogError(lineNumber, $"Group name did not end with '{closeCharacter}'");
                return null;
            }

            ParseWhitespace(reader, lineNumber, 0);

            return sb.ToString();
        }

        private void ParseWhitespace(TextReader reader, int lineNumber, int expectedNumSpaces)
        {
            int numSpaces = 0;
            char c;
            bool otherWhitespaceCharactersUed = false;
            while (reader.TryPeek(out c))
            {
                if (!Char.IsWhiteSpace(c))
                {
                    break;
                }

                reader.Read();

                if (c != ' ')
                {
                    otherWhitespaceCharactersUed = true;
                }
                numSpaces++;
            }
            if (otherWhitespaceCharactersUed)
            {
                _logger.LogWarning(lineNumber, "Non-space character used for whitespace");
            }
            else if (numSpaces != expectedNumSpaces)
            {
                if (expectedNumSpaces == 0)
                {
                    _logger.LogWarning(lineNumber, "Unnecessary whitespace");
                }
                else
                {
                    _logger.LogWarning(lineNumber, "Un-recommended whitespace length.");
                }
            }
        }
    }
}
