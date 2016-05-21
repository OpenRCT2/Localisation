using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace langcheck
{
    internal class LanguagePack
    {
        private Dictionary<int, LanguageEntry> _entries;

        public IReadOnlyDictionary<int, LanguageEntry> Entries => _entries;

        public LanguagePack(IEnumerable<LanguageEntry> entries)
        {
            _entries = new Dictionary<int, LanguageEntry>();
            foreach (LanguageEntry entry in entries)
            {
                if (!_entries.ContainsKey(entry.Id))
                {
                    _entries.Add(entry.Id, entry);
                }
            }
        }

        public static LanguagePack LoadFromFile(string path, IErrorLogger logger)
        {
            var parser = new LanguageParser(logger);
            using (var fs = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                var sr = new StreamReader(fs);

                var entries = new List<LanguageEntry>();
                int lineNumber = 1;
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    LanguageEntry entry = parser.ParseLine(lineNumber, line);
                    if (entry != null)
                    {
                        entries.Add(entry);
                    }
                    lineNumber++;
                }

                return new LanguagePack(entries);
            }
        }
    }
}