;--------------------------------------------------------
; File Created by SLCC : free open source ANSI-C Compiler
; Version 3.6.0 #Sep 28 2025 (MSVC)
;--------------------------------------------------------
; SL port for the RISC core
;--------------------------------------------------------
;	.file	"D:\POOLBULE0\芯片代码模板\C_1521\KEY.C"
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
	global	_keyProcess
	global	_keyScan
	global	_keyLongCnt
	global	_keyValOld
	global	_keyState
	global	_keyShake

;--------------------------------------------------------
; global definitions
;--------------------------------------------------------
;--------------------------------------------------------
; absolute symbol definitions
;--------------------------------------------------------
;--------------------------------------------------------
; compiler-defined variables
;--------------------------------------------------------
UDL_KEY_0	udata
r0x1006	res	1
r0x1007	res	1
r0x1008	res	1
r0x1009	res	1
r0x100A	res	1
_keyProcess_light_2_26	res	1
;--------------------------------------------------------
; initialized data
;--------------------------------------------------------

ID_KEY_0	idata
_keyLongCnt
	add 0x02,a
	db	0x00


ID_KEY_1	idata
_keyValOld
	add 0x02,a
	db	0x00


ID_KEY_2	idata
_keyState
	add 0x02,a
	db	0x00


ID_KEY_3	idata
_keyShake
	add 0x02,a
	db	0x00


;@Allocation info for local variables in function 'keyScan'
;@keyScan fw_pwm1Init               Allocated to registers ;size:2
;@keyScan fw_pwm2Init               Allocated to registers ;size:2
;@keyScan fw_pwm3Init               Allocated to registers ;size:2
;@keyScan fw_sleepEvent             Allocated to registers ;size:2
;@keyScan fw_clrRam                 Allocated to registers ;size:2
;@keyScan fw_gpioInit               Allocated to registers ;size:2
;@keyScan fw_tc0Init                Allocated to registers ;size:2
;@keyScan keyProcess                Allocated to registers ;size:2
;@keyScan IARbits                   Allocated to registers ;size:1
;@keyScan TCCbits                   Allocated to registers ;size:1
;@keyScan PCLbits                   Allocated to registers ;size:1
;@keyScan STATUSbits                Allocated to registers ;size:1
;@keyScan RSRbits                   Allocated to registers ;size:1
;@keyScan PORT5bits                 Allocated to registers ;size:1
;@keyScan PORT6bits                 Allocated to registers ;size:1
;@keyScan LVDCONbits                Allocated to registers ;size:1
;@keyScan PWMCONbits                Allocated to registers ;size:1
;@keyScan PRDbits                   Allocated to registers ;size:1
;@keyScan PDC1bits                  Allocated to registers ;size:1
;@keyScan PDC2bits                  Allocated to registers ;size:1
;@keyScan PDC3bits                  Allocated to registers ;size:1
;@keyScan ICIECRbits                Allocated to registers ;size:1
;@keyScan CPUCONbits                Allocated to registers ;size:1
;@keyScan ISRbits                   Allocated to registers ;size:1
;@keyScan U_Flage                   Allocated to registers ;size:1
;@keyScan r_g_workMod               Allocated to registers ;size:1
;@keyScan keyLongCnt                Allocated to registers ;size:1
;@keyScan keyValOld                 Allocated to registers ;size:1
;@keyScan keyState                  Allocated to registers ;size:1
;@keyScan keyShake                  Allocated to registers ;size:1
;@keyScan keyVal                    Allocated to registers r0x1006 ;size:1
;@keyScan keyEvent                  Allocated to registers r0x1007 ;size:1
;@keyScan IAR                       Allocated to registers ;size:1
;@keyScan TCC                       Allocated to registers ;size:1
;@keyScan PCL                       Allocated to registers ;size:1
;@keyScan STATUS                    Allocated to registers ;size:1
;@keyScan RSR                       Allocated to registers ;size:1
;@keyScan PORT5                     Allocated to registers ;size:1
;@keyScan PORT6                     Allocated to registers ;size:1
;@keyScan LVDCON                    Allocated to registers ;size:1
;@keyScan PWMCON                    Allocated to registers ;size:1
;@keyScan PRD                       Allocated to registers ;size:1
;@keyScan PDC1                      Allocated to registers ;size:1
;@keyScan PDC2                      Allocated to registers ;size:1
;@keyScan PDC3                      Allocated to registers ;size:1
;@keyScan ICIECR                    Allocated to registers ;size:1
;@keyScan CPUCON                    Allocated to registers ;size:1
;@keyScan ISR                       Allocated to registers ;size:1
;@end Allocation info for local variables in function 'keyScan';
;@Allocation info for local variables in function 'keyProcess'
;@keyProcess keyEvent                  Allocated to registers r0x1008 ;size:1
;@keyProcess light                     Allocated to registers ;size:1
;@end Allocation info for local variables in function 'keyProcess';
;@Allocation info for local variables in function 'keyProcess'
;@keyProcess keyEvent                  Allocated to registers r0x1008 ;size:1
;@keyProcess light                     Allocated to registers ;size:1
;@end Allocation info for local variables in function 'keyProcess';

;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;	udata_ovr
;--------------------------------------------------------
; code
;--------------------------------------------------------
code_KEY	code
;***
;  pBlock Stats: dbName = C
;***
;has an exit
;functions called:
;   _keyScan
;   _keyScan
;3 compiler assigned registers:
;   r0x1008
;   r0x1009
;   r0x100A
;; Starting pCode block
S_KEY__keyProcess	code
_keyProcess:	;Function start
; 2 exit points
;	.line	109; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	uint8_t keyEvent = keyScan();
	CALL	_keyScan
	MOV	r0x1008,A
;	.line	112; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(keyEvent & 0x80)  // 短按
	JBTS	r0x1008,7
	JMP	_00140_DS_
;	.line	114; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	F_CHARGE ^= 1;   // 切换充电状态
	CLR	r0x1009
	JBTC	_U_Flage,1
	INC	r0x1009
	MOV	A,r0x1009
	MOV	r0x100A,A
	MOV	A,@0x01
	XOR	A,r0x100A
	MOV	r0x100A,A
	MOV	r0x1009,A
;;103	MOV	A,r0x1009
	RCA	r0x100A
	JBTS	STATUS,0
	BTC	_U_Flage,1
	JBTC	STATUS,0
	BTS	_U_Flage,1
;	.line	115; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	PORT6_5 ^= 1;    // 切换LED指示
	CLR	r0x1009
	JBTC	_PORT6bits,5
	INC	r0x1009
	MOV	A,r0x1009
	MOV	r0x100A,A
	MOV	A,@0x01
	XOR	A,r0x100A
	MOV	r0x100A,A
	MOV	r0x1009,A
;;102	MOV	A,r0x1009
	RCA	r0x100A
	JBTS	STATUS,0
	BTC	_PORT6bits,5
	JBTC	STATUS,0
	BTS	_PORT6bits,5
_00140_DS_:
;	.line	119; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(keyEvent & 0x40)  // 长按
	JBTS	r0x1008,6
	JMP	_00155_DS_
;	.line	122; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(PDC1 >= 0x64)
	MOV	A,@0x64
	SUB	A,_PDC1
	JBTS	STATUS,0
	JMP	_00142_DS_
;	.line	124; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	dir = 0;
	BTC	_U_Flage,4
	JMP	_00143_DS_
_00142_DS_:
;	.line	128; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	dir = 1;
	BTS	_U_Flage,4
_00143_DS_:
;	.line	131; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(dir == 1)
	CLR	r0x1008
	JBTC	_U_Flage,4
	INC	r0x1008
;;101	MOV	A,r0x1008
;;100	MOV	A,r0x1009
	MOV	A,r0x1008
	MOV	r0x1009,A
	XOR	A,@0x01
	JBTS	STATUS,2
	JMP	_00151_DS_
;;swapping arguments (AOP_TYPEs 1/3)
;	.line	134; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(light <= 100)  // 防止溢出
	MOV	A,@0x65
	SUB	A,_keyProcess_light_2_26
	JBTC	STATUS,0
	JMP	_00145_DS_
;	.line	135; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	light += 10;
	MOV	A,@0x0a
	ADD	_keyProcess_light_2_26,A
	JMP	_00152_DS_
_00145_DS_:
;	.line	137; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	light = 100;
	MOV	A,@0x64
	MOV	_keyProcess_light_2_26,A
	JMP	_00152_DS_
_00151_DS_:
;	.line	142; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(light > 0)   // 防止下溢
	MOV	A,@0x00
	OR	A,_keyProcess_light_2_26
	JBTC	STATUS,2
	JMP	_00148_DS_
;	.line	143; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	light -= 10;
	MOV	A,@0xf6
	ADD	_keyProcess_light_2_26,A
	JMP	_00152_DS_
_00148_DS_:
;	.line	145; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	light = 0;
	CLR	_keyProcess_light_2_26
_00152_DS_:
;	.line	149; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	PDC1 = light;
	MOV	A,_keyProcess_light_2_26
	MOV	_PDC1,A
;	.line	151; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	PORT6_4 ^= 1;    // 切换LED指示
	CLR	r0x1008
	JBTC	_PORT6bits,4
	INC	r0x1008
	MOV	A,r0x1008
	MOV	r0x1009,A
	MOV	A,@0x01
	XOR	A,r0x1009
	MOV	r0x1009,A
	MOV	r0x1008,A
;;99	MOV	A,r0x1008
	RCA	r0x1009
	JBTS	STATUS,0
	BTC	_PORT6bits,4
	JBTC	STATUS,0
	BTS	_PORT6bits,4
;	.line	153; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	}
_00155_DS_:
	RET	
; exit point of _keyProcess

;***
;  pBlock Stats: dbName = C
;***
;has an exit
;2 compiler assigned registers:
;   r0x1006
;   r0x1007
;; Starting pCode block
S_KEY__keyScan	code
_keyScan:	;Function start
; 2 exit points
;	.line	13; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	uint8_t keyVal = 0;
	CLR	r0x1006
;	.line	14; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	uint8_t keyEvent = 0;
	CLR	r0x1007
;	.line	17; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(PORT6_0 == 0)
	JBTC	_PORT6bits,0
	JMP	_00106_DS_
;	.line	19; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyVal = 1;  // 按键按下
	MOV	A,@0x01
	MOV	r0x1006,A
;;swapping arguments (AOP_TYPEs 1/3)
_00106_DS_:
;	.line	22; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	switch(keyState)
	MOV	A,@0x04
	SUB	A,_keyState
	JBTC	STATUS,0
	JMP	_00133_DS_
	MOV	A,_keyState
	BANKSEL	PCL
	ADD	PCL,A
	JMP	_00107_DS_
	JMP	_00110_DS_
	JMP	_00116_DS_
	JMP	_00127_DS_
_00107_DS_:
;	.line	26; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	27; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyValOld = 0;
	CLR	_keyValOld
;	.line	28; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyLongCnt = 0;
	CLR	_keyLongCnt
;	.line	30; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(keyVal)
	MOV	A,@0x00
	OR	A,r0x1006
	JBTC	STATUS,2
	JMP	_00134_DS_
;	.line	32; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyValOld = keyVal;
	MOV	A,r0x1006
	MOV	_keyValOld,A
;	.line	33; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 1;  // 进入消抖状态
	MOV	A,@0x01
	MOV	_keyState,A
;	.line	35; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	break;
	JMP	_00134_DS_
_00110_DS_:
;	.line	39; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(keyVal == keyValOld)
	MOV	A,_keyValOld
	XOR	A,r0x1006
	JBTS	STATUS,2
	JMP	_00114_DS_
;	.line	41; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(++keyShake >= 3)  // 消抖3次
	INC	_keyShake
	MOV	A,@0x03
	SUB	A,_keyShake
	JBTS	STATUS,0
	JMP	_00134_DS_
;	.line	43; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	44; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 2;  // 进入长按检测
	MOV	A,@0x02
	MOV	_keyState,A
	JMP	_00134_DS_
_00114_DS_:
;	.line	49; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 0;  // 按键抖动，返回初始状态
	CLR	_keyState
;	.line	51; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	break;
	JMP	_00134_DS_
_00116_DS_:
;	.line	55; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(keyVal == keyValOld)
	MOV	A,_keyValOld
	XOR	A,r0x1006
	JBTS	STATUS,2
	JMP	_00125_DS_
;	.line	57; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	58; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(++keyLongCnt >= 200)  // 长按时间约2秒
	INC	_keyLongCnt
	MOV	A,@0xc8
	SUB	A,_keyLongCnt
	JBTS	STATUS,0
	JMP	_00134_DS_
;	.line	60; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyLongCnt = 0;
	CLR	_keyLongCnt
;	.line	61; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyEvent = 0x40;  // 长按事件
	MOV	A,@0x40
	MOV	r0x1007,A
;	.line	62; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 3;     // 进入等待抬起状态
	MOV	A,@0x03
	MOV	_keyState,A
	JMP	_00134_DS_
_00125_DS_:
;	.line	65; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	else if(keyVal == 0)
	MOV	A,@0x00
	OR	A,r0x1006
	JBTS	STATUS,2
	JMP	_00122_DS_
;	.line	67; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(++keyShake >= 3)
	INC	_keyShake
	MOV	A,@0x03
	SUB	A,_keyShake
	JBTS	STATUS,0
	JMP	_00134_DS_
;	.line	69; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	70; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyEvent = 0x80;  // 短按事件
	MOV	A,@0x80
	MOV	r0x1007,A
;	.line	71; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 0;     // 返回初始状态
	CLR	_keyState
	JMP	_00134_DS_
_00122_DS_:
;	.line	76; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	77; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 0;  // 异常情况
	CLR	_keyState
;	.line	79; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	break;
	JMP	_00134_DS_
_00127_DS_:
;	.line	83; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyValOld = 0;
	CLR	_keyValOld
;	.line	84; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(keyVal == 0)
	MOV	A,@0x00
	OR	A,r0x1006
	JBTS	STATUS,2
	JMP	_00131_DS_
;	.line	86; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	if(++keyShake >= 3)
	INC	_keyShake
	MOV	A,@0x03
	SUB	A,_keyShake
	JBTS	STATUS,0
	JMP	_00134_DS_
;	.line	88; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	89; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 0;  // 按键抬起，返回初始状态
	CLR	_keyState
	JMP	_00134_DS_
_00131_DS_:
;	.line	94; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyShake = 0;
	CLR	_keyShake
;	.line	96; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	break;
	JMP	_00134_DS_
_00133_DS_:
;	.line	99; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	keyState = 0;
	CLR	_keyState
_00134_DS_:
;	.line	103; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	return keyEvent;
	MOV	A,r0x1007
;	.line	104; D:\POOLBULE0\芯片代码模板\C_1521\KEY.C	}
	RET	
; exit point of _keyScan


;	code size estimation:
;	  178+    1 =   179 instructions (  360 byte)

	end
