SYSTEM_INFO SysGuide;
GetSystemInfo(&SysGuide);

int CoreNum = SysGuide.dwNumberOfProcessors;
if (CoreNum < 2)
{
    exit(0);
}