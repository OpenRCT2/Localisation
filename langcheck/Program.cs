using System;
using System.IO;

namespace langcheck
{
    public class Program
    {
        private static class ExitCodes
        {
            public const int Fatal = -1;
            public const int OK = 0;
            public const int UsageInfo = 1;
            public const int Errors = 2;
            public const int Warnings = 3;
        }

        public static int Main(string[] args)
        {
            try
            {
                var logger = new Logger();
                if (args.Length == 1)
                {
                    string packPath = args[0];
                    WriteLine($"Parsing {packPath}", ConsoleColor.Cyan);
                    var basePack = LanguagePack.LoadFromFile(packPath, logger);
                }
                else if (args.Length == 2)
                {
                    string basePackPath = args[0];
                    string translationPackPath = args[1];

                    var basePack = LanguagePack.LoadFromFile(basePackPath, new FakeLogger());

                    WriteLine($"Parsing {translationPackPath}", ConsoleColor.Cyan);
                    var translationPack = LanguagePack.LoadFromFile(translationPackPath, logger);

                    foreach (var kvp in basePack.Entries)
                    {
                        int id = kvp.Key;
                        string baseString = kvp.Value.Text;
                        if (!translationPack.Entries.ContainsKey(id))
                        {
                            string message = String.Format("No string for STR_{0:0000}:    {1}", id, baseString);
                            WriteLine(message, ConsoleColor.Yellow);
                        }
                    }
                }
                else
                {
                    PrintUsageInfo();
                    return ExitCodes.UsageInfo;
                }

                if (logger.HasErrors)
                {
                    Console.WriteLine();
                    return ExitCodes.Errors;
                }
                else if (logger.HasWarnings)
                {
                    Console.WriteLine();
                    return ExitCodes.Warnings;
                }
            }
            catch (IOException ex)
            {
                WriteLine($"Unable to open file: {ex.Message}", ConsoleColor.Red);
                return ExitCodes.Fatal;
            }
            return ExitCodes.OK;
        }
        
        private static void PrintUsageInfo()
        {
            WriteLine("OpenRCT2 Language Checker", ConsoleColor.Cyan);
            WriteLine("Version 1.0", ConsoleColor.Cyan);
            WriteLine("");
            WriteLine("usage: langcheck <base language path> <translation language path>");
        }
        
        private static void WriteLine(string s, ConsoleColor? colour = null)
        {
            ConsoleColor originalForegroundColour = default(ConsoleColor);
            
            if (colour.HasValue)
            {
                originalForegroundColour = Console.ForegroundColor;
                Console.ForegroundColor = colour.Value;
            }
            
            Console.WriteLine(s);
            
            if (colour.HasValue)
            {
                Console.ForegroundColor = originalForegroundColour;
            }
        }

        private class Logger : IErrorLogger
        {
            public bool HasWarnings { get; private set; }
            public bool HasErrors { get; private set; }

            public void LogWarning(int lineNumber, string message)
            {
                WriteLine($"  warning: Line {lineNumber}: {message}", ConsoleColor.Yellow);
                HasWarnings = true;
            }

            public void LogError(int lineNumber, string message)
            {
                WriteLine($"  error:   Line {lineNumber}: {message}", ConsoleColor.Red);
                HasErrors = true;
            }
        }

        private class FakeLogger : IErrorLogger
        {
            public void LogError(int lineNumber, string message) { }
            public void LogWarning(int lineNumber, string message) { }
        }
    }
}
