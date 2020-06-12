int op1= 6381;
int i = 0;

for (i = 0; i < op1; i++)
{
    printf("%d\n", i);

    char * mem1 = NULL;
    mem1 = (char * )malloc(48407786);

    if (mem1 != NULL)
    {
        memset(mem1, 00, 48407786);
        free(mem1);
    }
    else{exit(0);}
}
if (i != op1)
{
    exit(0);
}
