namespace langcheck
{
    internal interface IErrorLogger
    {
        void LogWarning(int lineNumber, string message);
        void LogError(int lineNumber, string message);
    }
}