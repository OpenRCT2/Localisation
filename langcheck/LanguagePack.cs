using System.Collections.Generic;
using System.IO;

namespace langcheck
{
    internal class LanguagePack
    {
        public LanguagePack(IEnumerable<LanguageEntry> entries)
        {
            
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