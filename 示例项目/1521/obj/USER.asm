;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"D:\POOLBULE0\芯片代码模板\C_1521\USER.C"
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
	extern	_U_Flage
	extern	_r_g_workMod
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

	extern STK06
	extern STK05
	extern STK04
	extern STK03
	extern STK02
	extern STK01
	extern STK00
;--------------------------------------------------------
; global declarations
;--------------------------------------------------------
	global	_fw_gpioInit
	global	_fw_clrRam

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

;@Allocation info for local variables in function 'fw_clrRam'
;@fw_clrRam fw_pwm1Init               Allocated to registers ;size:2
;@fw_clrRam fw_pwm2Init               Allocated to registers ;size:2
;@fw_clrRam fw_pwm3Init               Allocated to registers ;size:2
;@fw_clrRam fw_sleepEvent             Allocated to registers ;size:2
;@fw_clrRam keyScan                   Allocated to registers ;size:2
;@fw_clrRam keyProcess                Allocated to registers ;size:2
;@fw_clrRam fw_gpioInit               Allocated to registers ;size:2
;@fw_clrRam fw_tc0Init                Allocated to registers ;size:2
;@fw_clrRam IARbits                   Allocated to registers ;size:1
;@fw_clrRam TCCbits                   Allocated to registers ;size:1
;@fw_clrRam PCLbits                   Allocated to registers ;size:1
;@fw_clrRam STATUSbits                Allocated to registers ;size:1
;@fw_clrRam RSRbits                   Allocated to registers ;size:1
;@fw_clrRam PORT5bits                 Allocated to registers ;size:1
;@fw_clrRam PORT6bits                 Allocated to registers ;size:1
;@fw_clrRam LVDCONbits                Allocated to registers ;size:1
;@fw_clrRam PWMCONbits                Allocated to registers ;size:1
;@fw_clrRam PRDbits                   Allocated to registers ;size:1
;@fw_clrRam PDC1bits                  Allocated to registers ;size:1
;@fw_clrRam PDC2bits                  Allocated to registers ;size:1
;@fw_clrRam PDC3bits                  Allocated to registers ;size:1
;@fw_clrRam ICIECRbits                Allocated to registers ;size:1
;@fw_clrRam CPUCONbits                Allocated to registers ;size:1
;@fw_clrRam ISRbits                   Allocated to registers ;size:1
;@fw_clrRam U_Flage                   Allocated to registers ;size:1
;@fw_clrRam r_g_workMod               Allocated to registers ;size:1
;@fw_clrRam IAR                       Allocated to registers ;size:1
;@fw_clrRam TCC                       Allocated to registers ;size:1
;@fw_clrRam PCL                       Allocated to registers ;size:1
;@fw_clrRam STATUS                    Allocated to registers ;size:1
;@fw_clrRam RSR                       Allocated to registers ;size:1
;@fw_clrRam PORT5                     Allocated to registers ;size:1
;@fw_clrRam PORT6                     Allocated to registers ;size:1
;@fw_clrRam LVDCON                    Allocated to registers ;size:1
;@fw_clrRam PWMCON                    Allocated to registers ;size:1
;@fw_clrRam PRD                       Allocated to registers ;size:1
;@fw_clrRam PDC1                      Allocated to registers ;size:1
;@fw_clrRam PDC2                      Allocated to registers ;size:1
;@fw_clrRam PDC3                      Allocated to registers ;size:1
;@fw_clrRam ICIECR                    Allocated to registers ;size:1
;@fw_clrRam CPUCON                    Allocated to registers ;size:1
;@fw_clrRam ISR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'fw_clrRam';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_USER	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_USER__fw_gpioInit	code
_fw_gpioInit:	;Function start
; 2 exit points
;	.line	18; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IOCP_W(P5CR,0x00);		//P5口设为输出
	mov	a,@0x00
	iw	P5CR
;	.line	19; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	PORT5 = 0;				//P5口输出低
	CLR	_PORT5
;	.line	21; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IOCP_W(P6CR,0x01);		//P6口设为输出
	mov	a,@0x01
	iw	P6CR
;	.line	22; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	PORT6 = 0;				//P6口输出低
	CLR	_PORT6
;	.line	24; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IOCP_W(PHDCR,0xff);		//端口上下拉控制寄存器，bit7-bit4对应P67-P64下拉;bit3-bit0对应P53-P50上拉 
	mov	a,@0xff
	iw	PHDCR
;	.line	25; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IOCP_W(PDCR,0xff);		//端口下拉控制寄存器，  bit6-bit4对应P62-P60,bit3-bit0对应P53-P50
	mov	a,@0xff
	iw	PDCR
;	.line	27; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IOCP_W(PHCR,0xfe);		//P6端口上拉控制寄存?? bit7-bit0对应P67-P60
	mov	a,@0xfe
	iw	PHCR
;	.line	29; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IOCP_W(WDTCR,0x00);		//WDT 使能控制寄存??
	mov	a,@0x00
	iw	WDTCR
;	.line	31; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	ICIECR=0X00;		//P63端口独立唤醒
	CLR	_ICIECR
;	.line	32; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	}
	RET	
; exit point of _fw_gpioInit

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;; Starting pCode block
S_USER__fw_clrRam	code
_fw_clrRam:	;Function start
; 2 exit points
;	.line	8; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	for(RSR=0x90;RSR<0xFF;RSR++)	//清零 BANK0 RAM  IAR-R0,RSR-R4
	MOV	A,@0x90
	MOV	_RSR,A
_00107_DS_:
	MOV	A,@0xff
	SUB	A,_RSR
	JBTC	STATUS,0
	JMP	_00105_DS_
;	.line	9; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	{IAR = 0;}
	CLR	_IAR
;	.line	8; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	for(RSR=0x90;RSR<0xFF;RSR++)	//清零 BANK0 RAM  IAR-R0,RSR-R4
	INC	_RSR
	JMP	_00107_DS_
_00105_DS_:
;	.line	10; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	IAR = 0;
	CLR	_IAR
;	.line	11; D:\POOLBULE0\芯片代码模板\C_1521\USER.C	}
	RET	
; exit point of _fw_clrRam


;	code size estimation:
;	   15+    0 =    15 instructions (   30 byte)

	end
