LPVOID mem = NULL;
mem = VirtualAllocExNuma(GetCurrentProcess(), NULL, 1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE, 0);
if (mem != NULL)
{
	printf("Hello World\n");
}
else
{
	exit(0);
}