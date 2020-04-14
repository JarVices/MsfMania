char * MEMDMP1 = NULL;
MEMDMP1 = (char *)malloc(300000000);
if (MEMDMP1 != NULL) 
{
    memset(MEMDMP1, 00, 300000000);
}
int TICK1 = GetTickCount();
Sleep(1000);
int TAC1 = GetTickCount();
if ((TAC1 - TICK1) < 1000) 
{
    exit(0);
}
free(MEMDMP1);

