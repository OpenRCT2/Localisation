using System;
using System.IO;

namespace langcheck.Extensions
{
    internal static class StringReaderExtensions
    {
        public static bool TryPeek(this TextReader reader, out char c)
        {
            int readCharacter = reader.Peek();
            if (readCharacter != -1)
            {
                c = (char)readCharacter;
                return true;
            }
            else
            {
                c = '\0';
                return false;
            }
        }

        public static bool TryRead(this TextReader reader, out char c)
        {
            int readCharacter = reader.Read();
            if (readCharacter != -1)
            {
                c = (char)readCharacter;
                return true;
            }
            else
            {
                c = '\0';
                return false;
            }
        }

        public static string ReadString(this TextReader reader, int length)
        {
            char[] buffer = new char[length];
            int readLength = reader.ReadBlock(buffer, 0, length);
            return new String(buffer, 0, readLength);
        }

        public static bool TryReadExpected(this TextReader reader, string expectedString)
        {
            return ReadString(reader, expectedString.Length) == expectedString;
        }
    }
}
