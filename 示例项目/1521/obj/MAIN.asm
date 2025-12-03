;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C"
	list	p=JZ8P1521
	radix dec
	include "JZ8P1521.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_fw_pwm1Init
	extern	_fw_pwm2Init
	extern	_fw_pwm3Init
	extern	_fw_sleepEvent
	extern	_keyScan
	extern	_keyProcess
	extern	_fw_clrRam
	extern	_fw_gpioInit
	extern	_fw_tc0Init
	extern	_IARbits
	extern	_TCCbits
	extern	_PCLbits
	extern	_STATUSbits
	extern	_RSRbits
	extern	_PORT5bits
	extern	_PORT6bits
	extern	_LVDCONbits
	extern	_PWMCONbits
	extern	_PRDbits
	extern	_PDC1bits
	extern	_PDC2bits
	extern	_PDC3bits
	extern	_ICIECRbits
	extern	_CPUCONbits
	extern	_ISRbits
	extern	_IAR
	extern	_TCC
	extern	_PCL
	extern	_STATUS
	extern	_RSR
	extern	_PORT5
	extern	_PORT6
	extern	_LVDCON
	extern	_PWMCON
	extern	_PRD
	extern	_PDC1
	extern	_PDC2
	extern	_PDC3
	extern	_ICIECR
	extern	_CPUCON
	extern	_ISR
;--------------------------------------------------------
; global declarations
;--------------------------------------------------------
	global	_main
	global	_U_Flage
	global	_r_g_workMod

	global STK06
	global STK05
	global STK04
	global STK03
	global STK02
	global STK01
	global STK00

sharebank udata_ovr 0x0020
STK06	res 1
STK05	res 1
STK04	res 1
STK03	res 1
STK02	res 1
STK01	res 1
STK00	res 1

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
UD_MAIN_0	udata
_U_Flage	res	1

UD_MAIN_1	udata
_r_g_workMod	res	1

;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'main'
;@main fw_pwm1Init               Allocated to registers ;size:2
;@main fw_pwm2Init               Allocated to registers ;size:2
;@main fw_pwm3Init               Allocated to registers ;size:2
;@main fw_sleepEvent             Allocated to registers ;size:2
;@main keyScan                   Allocated to registers ;size:2
;@main keyProcess                Allocated to registers ;size:2
;@main fw_clrRam                 Allocated to registers ;size:2
;@main fw_gpioInit               Allocated to registers ;size:2
;@main fw_tc0Init                Allocated to registers ;size:2
;@main main                      Allocated to registers ;size:2
;@main IARbits                   Allocated to registers ;size:1
;@main TCCbits                   Allocated to registers ;size:1
;@main PCLbits                   Allocated to registers ;size:1
;@main STATUSbits                Allocated to registers ;size:1
;@main RSRbits                   Allocated to registers ;size:1
;@main PORT5bits                 Allocated to registers ;size:1
;@main PORT6bits                 Allocated to registers ;size:1
;@main LVDCONbits                Allocated to registers ;size:1
;@main PWMCONbits                Allocated to registers ;size:1
;@main PRDbits                   Allocated to registers ;size:1
;@main PDC1bits                  Allocated to registers ;size:1
;@main PDC2bits                  Allocated to registers ;size:1
;@main PDC3bits                  Allocated to registers ;size:1
;@main ICIECRbits                Allocated to registers ;size:1
;@main CPUCONbits                Allocated to registers ;size:1
;@main ISRbits                   Allocated to registers ;size:1
;@main U_Flage                   Allocated to registers ;size:1
;@main r_g_workMod               Allocated to registers ;size:1
;@main IAR                       Allocated to registers ;size:1
;@main TCC                       Allocated to registers ;size:1
;@main PCL                       Allocated to registers ;size:1
;@main STATUS                    Allocated to registers ;size:1
;@main RSR                       Allocated to registers ;size:1
;@main PORT5                     Allocated to registers ;size:1
;@main PORT6                     Allocated to registers ;size:1
;@main LVDCON                    Allocated to registers ;size:1
;@main PWMCON                    Allocated to registers ;size:1
;@main PRD                       Allocated to registers ;size:1
;@main PDC1                      Allocated to registers ;size:1
;@main PDC2                      Allocated to registers ;size:1
;@main PDC3                      Allocated to registers ;size:1
;@main ICIECR                    Allocated to registers ;size:1
;@main CPUCON                    Allocated to registers ;size:1
;@main ISR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'main';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; reset vector 
;--------------------------------------------------------
STARTUP	code 0x0000
	jmp	_main
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_MAIN	code
;***
;  pBlock Stats: dbName = M
;***
;has an exit
;functions called:
;   _fw_clrRam
;   _fw_gpioInit
;   _fw_tc0Init
;   _fw_pwm1Init
;   _fw_sleepEvent
;   _keyProcess
;   _fw_clrRam
;   _fw_gpioInit
;   _fw_tc0Init
;   _fw_pwm1Init
;   _fw_sleepEvent
;   _keyProcess
;; Starting pCode block
S_MAIN__main	code
_main:	;Function start
; 2 exit points
;	.line	8; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	fw_clrRam();		//清RAM
	CALL	_fw_clrRam
;	.line	9; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	fw_gpioInit();		//端口初始化
	CALL	_fw_gpioInit
;	.line	10; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	fw_tc0Init();		//定时器初始化
	CALL	_fw_tc0Init
;	.line	11; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	fw_pwm1Init();
	CALL	_fw_pwm1Init
;	.line	13; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	EI();				//开启中断
	ei	
_00108_DS_:
;	.line	16; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	if (Time_10ms)
	JBTS	_U_Flage,0
	JMP	_00108_DS_
;	.line	18; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	Time_10ms = DISABLE;
	BTC	_U_Flage,0
;	.line	19; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	fw_sleepEvent();
	CALL	_fw_sleepEvent
;	.line	20; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	keyProcess();
	CALL	_keyProcess
	JMP	_00108_DS_
;	.line	25; D:\POOLBULE0\芯片代码模板\C_1521\MAIN.C	}
	RET	
; exit point of _main


;	code size estimation:
;	   11+    0 =    11 instructions (   22 byte)

	end
