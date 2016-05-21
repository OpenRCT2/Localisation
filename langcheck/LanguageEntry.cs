using System;

namespace langcheck
{
    internal class LanguageEntry
    {
        public string Line { get; }

        public int Id { get; set; }
        public string Text { get; set; }

        public static bool TryParse(string line, out LanguageEntry entry)
        {
            entry = null;
            if (line.Length > 8)
            {
                string l = line.Substring(4, 4);
                int id;
                if (Int32.TryParse(l, out id))
                {
                    int colonOffset = line.IndexOf(':');
                    if (colonOffset != 0)
                    {
                        string text = line.Substring(colonOffset + 1);
                        entry = new LanguageEntry()
                        {
                            Id = id,
                            Text = text
                        };
                        return true;
                    }
                }
            }
            return false;
        }
    }
}