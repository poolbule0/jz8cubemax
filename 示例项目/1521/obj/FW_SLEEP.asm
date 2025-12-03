;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C"
	list	p=JZ8P1521
	radix dec
	include "JZ8P1521.inc"
;--------------------------------------------------------
; external declarations
;--------------------------------------------------------
	extern	_fw_pwm1Init
	extern	_fw_pwm2Init
	extern	_fw_pwm3Init
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
	global	_fw_sleepEvent
	global	_sleep_cnt

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_FW_SLEEP_0	udata
r0x1002	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

ID_FW_SLEEP_0	idata
_sleep_cnt
	add 0x02,a
	db	0x00


;@Allocation info for local variables in function 'fw_sleepEvent'
;@fw_sleepEvent fw_pwm1Init               Allocated to registers ;size:2
;@fw_sleepEvent fw_pwm2Init               Allocated to registers ;size:2
;@fw_sleepEvent fw_pwm3Init               Allocated to registers ;size:2
;@fw_sleepEvent keyScan                   Allocated to registers ;size:2
;@fw_sleepEvent keyProcess                Allocated to registers ;size:2
;@fw_sleepEvent fw_clrRam                 Allocated to registers ;size:2
;@fw_sleepEvent fw_gpioInit               Allocated to registers ;size:2
;@fw_sleepEvent fw_tc0Init                Allocated to registers ;size:2
;@fw_sleepEvent IARbits                   Allocated to registers ;size:1
;@fw_sleepEvent TCCbits                   Allocated to registers ;size:1
;@fw_sleepEvent PCLbits                   Allocated to registers ;size:1
;@fw_sleepEvent STATUSbits                Allocated to registers ;size:1
;@fw_sleepEvent RSRbits                   Allocated to registers ;size:1
;@fw_sleepEvent PORT5bits                 Allocated to registers ;size:1
;@fw_sleepEvent PORT6bits                 Allocated to registers ;size:1
;@fw_sleepEvent LVDCONbits                Allocated to registers ;size:1
;@fw_sleepEvent PWMCONbits                Allocated to registers ;size:1
;@fw_sleepEvent PRDbits                   Allocated to registers ;size:1
;@fw_sleepEvent PDC1bits                  Allocated to registers ;size:1
;@fw_sleepEvent PDC2bits                  Allocated to registers ;size:1
;@fw_sleepEvent PDC3bits                  Allocated to registers ;size:1
;@fw_sleepEvent ICIECRbits                Allocated to registers ;size:1
;@fw_sleepEvent CPUCONbits                Allocated to registers ;size:1
;@fw_sleepEvent ISRbits                   Allocated to registers ;size:1
;@fw_sleepEvent U_Flage                   Allocated to registers ;size:1
;@fw_sleepEvent r_g_workMod               Allocated to registers ;size:1
;@fw_sleepEvent sleep_cnt                 Allocated to registers ;size:1
;@fw_sleepEvent IAR                       Allocated to registers ;size:1
;@fw_sleepEvent TCC                       Allocated to registers ;size:1
;@fw_sleepEvent PCL                       Allocated to registers ;size:1
;@fw_sleepEvent STATUS                    Allocated to registers ;size:1
;@fw_sleepEvent RSR                       Allocated to registers ;size:1
;@fw_sleepEvent PORT5                     Allocated to registers ;size:1
;@fw_sleepEvent PORT6                     Allocated to registers ;size:1
;@fw_sleepEvent LVDCON                    Allocated to registers ;size:1
;@fw_sleepEvent PWMCON                    Allocated to registers ;size:1
;@fw_sleepEvent PRD                       Allocated to registers ;size:1
;@fw_sleepEvent PDC1                      Allocated to registers ;size:1
;@fw_sleepEvent PDC2                      Allocated to registers ;size:1
;@fw_sleepEvent PDC3                      Allocated to registers ;size:1
;@fw_sleepEvent ICIECR                    Allocated to registers ;size:1
;@fw_sleepEvent CPUCON                    Allocated to registers ;size:1
;@fw_sleepEvent ISR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'fw_sleepEvent';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_FW_SLEEP	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;functions called:
;   _fw_tc0Init
;   _fw_tc0Init
;1 compiler assigned register :
;   r0x1002
;; Starting pCode block
S_FW_SLEEP__fw_sleepEvent	code
_fw_sleepEvent:	;Function start
; 2 exit points
;	.line	5; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	if(F_CHARGE == 0)
	JBTC	_U_Flage,1
	JMP	_00109_DS_
;	.line	7; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	if(sleep_cnt++ > 10)
	MOV	A,_sleep_cnt
	MOV	r0x1002,A
	INC	_sleep_cnt
;;swapping arguments (AOP_TYPEs 1/2)
	MOV	A,@0x0b
	SUB	A,r0x1002
	JBTS	STATUS,0
	JMP	_00109_DS_
;	.line	9; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	sleep_cnt = 0;
	CLR	_sleep_cnt
;	.line	12; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	LVDCON = 0;// 关LVD
	CLR	_LVDCON
;	.line	14; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	IOCP_W(IMR,0x00);   //关闭中断
	mov	a,@0x00
	iw	IMR
;	.line	15; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	IOCP_W(WDTCR,0x00);	
	mov	a,@0x00
	iw	WDTCR
;	.line	16; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	ISR	=0;              // 清中断标志位
	CLR	_ISR
;	.line	17; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	DI();		         // 禁止唤醒进入中断
	di	
;	.line	18; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	IOCP_W(IMR,0x02);    //使能端口变化中断，不使能无法唤醒
	mov	a,@0x02
	iw	IMR
;	.line	19; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	SLEEP();
	sleep	
;	.line	20; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	NOP(); 
	nop	
;	.line	21; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	NOP();
	nop	
;	.line	22; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	NOP();
	nop	
;	.line	23; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	NOP();
	nop	
;	.line	24; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	CWDT();
	CWDT	
;	.line	30; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	IOCP_W(IMR,0x00);   //关闭中断
	mov	a,@0x00
	iw	IMR
;	.line	31; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	fw_tc0Init();
	CALL	_fw_tc0Init
;	.line	32; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	EI();
	ei	
;	.line	33; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	ISR=0;
	CLR	_ISR
;	.line	39; D:\POOLBULE0\芯片代码模板\C_1521\FW_SLEEP.C	}
_00109_DS_:
	RET	
; exit point of _fw_sleepEvent


;	code size estimation:
;	   15+    0 =    15 instructions (   30 byte)

	end
