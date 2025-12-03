#ifndef __JZ8P1521_H__
#define __JZ8P1521_H__

//
// Register addresses.
//
//RPAGE Bank0
#define IAR_ADDR         	0X00
#define TCC_ADDR         	0X01
#define PCL_ADDR          	0X02
#define STATUS_ADDR         	0X03
#define RSR_ADDR         	0X04
#define PORT5_ADDR        	0X05
#define PORT6_ADDR        	0X06
#define LVDCON_ADDR        	0X07
#define PWMCON_ADDR        	0X08
#define PRD_ADDR        	0X09
#define PDC1_ADDR        	0X0A
#define PDC2_ADDR        	0X0B
#define PDC3_ADDR        	0X0C
#define ICIECR_ADDR        	0X0D
#define CPUCON_ADDR        	0X0E
#define ISR_ADDR        	0X0F

//
//----- Register Files -----------------------------------------------------
//
extern __sfr __at (IAR_ADDR)        	IAR;         	
extern __sfr __at (TCC_ADDR)        	TCC;         	
extern __sfr __at (PCL_ADDR)        	PCL;          	
extern __sfr __at (STATUS_ADDR)        	STATUS;         	
extern __sfr __at (RSR_ADDR)        	RSR;
extern __sfr __at (PORT5_ADDR)        	PORT5;         	
extern __sfr __at (PORT6_ADDR)        	PORT6;         	
extern __sfr __at (LVDCON_ADDR)       	LVDCON;        	
extern __sfr __at (PWMCON_ADDR)       	PWMCON;        	
extern __sfr __at (PRD_ADDR)		PRD;        	
extern __sfr __at (PDC1_ADDR)       	PDC1;        	
extern __sfr __at (PDC2_ADDR)       	PDC2;        	
extern __sfr __at (PDC3_ADDR)       	PDC3;        	
extern __sfr __at (ICIECR_ADDR)       	ICIECR;        	
extern __sfr __at (CPUCON_ADDR)       	CPUCON;        	
extern __sfr __at (ISR_ADDR)       	ISR;        	     	
//==========================================================================
//
//	Configuration Bits
//
//==========================================================================

// ----- IAR Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char IAR_0:1;
		unsigned char IAR_1:1;
		unsigned char IAR_2:1;
		unsigned char IAR_3:1;	
		unsigned char IAR_4:1;
		unsigned char IAR_5:1;
		unsigned char IAR_6:1;
		unsigned char IAR_7:1;		
	};
} __IARbits_t;
extern volatile __IARbits_t __at(IAR_ADDR) IARbits;

#define IAR_0         	IARbits.IAR_0   	/* bit 0 */
#define IAR_1         	IARbits.IAR_1     	/* bit 1 */
#define IAR_2         	IARbits.IAR_2       /* bit 2 */
#define IAR_3         	IARbits.IAR_3       /* bit 3 */
#define IAR_4         	IARbits.IAR_4   	/* bit 4 */
#define IAR_5         	IARbits.IAR_5     	/* bit 5 */
#define IAR_6         	IARbits.IAR_6       /* bit 6 */
#define IAR_7         	IARbits.IAR_7       /* bit 7 */

// ----- TCC Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TCC_0:1;
		unsigned char TCC_1:1;
		unsigned char TCC_2:1;
		unsigned char TCC_3:1;	
		unsigned char TCC_4:1;
		unsigned char TCC_5:1;
		unsigned char TCC_6:1;
		unsigned char TCC_7:1;		
	};
} __TCCbits_t;
extern volatile __TCCbits_t __at(TCC_ADDR) TCCbits;

#define TCC_0         	TCCbits.TCC_0   	/* bit 0 */
#define TCC_1         	TCCbits.TCC_1     	/* bit 1 */
#define TCC_2         	TCCbits.TCC_2       /* bit 2 */
#define TCC_3         	TCCbits.TCC_3       /* bit 3 */
#define TCC_4         	TCCbits.TCC_4   	/* bit 4 */
#define TCC_5         	TCCbits.TCC_5     	/* bit 5 */
#define TCC_6         	TCCbits.TCC_6       /* bit 6 */
#define TCC_7         	TCCbits.TCC_7       /* bit 7 */

// ----- PCL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PCL_0:1;
		unsigned char PCL_1:1;
		unsigned char PCL_2:1;
		unsigned char PCL_3:1;	
		unsigned char PCL_4:1;
		unsigned char PCL_5:1;
		unsigned char PCL_6:1;
		unsigned char PCL_7:1;		
	};
} __PCLbits_t;
extern volatile __PCLbits_t __at(PCL_ADDR) PCLbits;

#define PCL_0         	PCLbits.PCL_0   	/* bit 0 */
#define PCL_1         	PCLbits.PCL_1     	/* bit 1 */
#define PCL_2         	PCLbits.PCL_2       /* bit 2 */
#define PCL_3         	PCLbits.PCL_3       /* bit 3 */
#define PCL_4         	PCLbits.PCL_4   	/* bit 4 */
#define PCL_5         	PCLbits.PCL_5     	/* bit 5 */
#define PCL_6         	PCLbits.PCL_6       /* bit 6 */
#define PCL_7         	PCLbits.PCL_7       /* bit 7 */

// ----- STATUS Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char STATUS_0:1;
		unsigned char STATUS_1:1;
		unsigned char STATUS_2:1;
		unsigned char STATUS_3:1;	
		unsigned char STATUS_4:1;
		unsigned char STATUS_5:1;
		unsigned char STATUS_6:1;
		unsigned char STATUS_7:1;		
	};
} __STATUSbits_t;
extern volatile __STATUSbits_t __at(STATUS_ADDR) STATUSbits;

#define C		STATUSbits.STATUS_0   	/* bit 0 */
#define DC		STATUSbits.STATUS_1		/* bit 1 */
#define Z		STATUSbits.STATUS_2		/* bit 2 */
#define P		STATUSbits.STATUS_3	    /* bit 3 */
#define T		STATUSbits.STATUS_4   	/* bit 4 */
#define GB0         	STATUSbits.STATUS_5	    /* bit 5 */
#define GB1         	STATUSbits.STATUS_6	    /* bit 6 */
#define RST         	STATUSbits.STATUS_7	    /* bit 7 */

// ----- RSR Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char RSR_0:1;
		unsigned char RSR_1:1;
		unsigned char RSR_2:1;
		unsigned char RSR_3:1;	
		unsigned char RSR_4:1;
		unsigned char RSR_5:1;
		unsigned char RSR_6:1;
		unsigned char RSR_7:1;		
	};
} __RSRbits_t;
extern volatile __RSRbits_t __at(RSR_ADDR) RSRbits;

#define RSR_0         	RSRbits.RSR_0   	/* bit 0 */
#define RSR_1         	RSRbits.RSR_1    	/* bit 1 */
#define RSR_2         	RSRbits.RSR_2    	/* bit 2 */
#define RSR_3         	RSRbits.RSR_3    	/* bit 3 */
#define RSR_4         	RSRbits.RSR_4   	/* bit 4 */
#define RSR_5         	RSRbits.RSR_5    	/* bit 5 */
#define RSR_6         	RSRbits.RSR_6    	/* bit 6 */
#define RSR_7         	RSRbits.RSR_7    	/* bit 7 */

// ----- PORT5 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PORT5_0:1;
		unsigned char PORT5_1:1;
		unsigned char PORT5_2:1;
		unsigned char PORT5_3:1;	
		unsigned char PORT5_4:1;
		unsigned char PORT5_5:1;
		unsigned char PORT5_6:1;
		unsigned char PORT5_7:1;		
	};
} __PORT5bits_t;
extern volatile __PORT5bits_t __at(PORT5_ADDR) PORT5bits;

#define PORT5_0         PORT5bits.PORT5_0   	/* bit 0 */
#define PORT5_1         PORT5bits.PORT5_1     	/* bit 1 */
#define PORT5_2         PORT5bits.PORT5_2       /* bit 2 */
#define PORT5_3         PORT5bits.PORT5_3       /* bit 3 */

// ----- PORT6 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PORT6_0:1;
		unsigned char PORT6_1:1;
		unsigned char PORT6_2:1;
		unsigned char PORT6_3:1;	
		unsigned char PORT6_4:1;
		unsigned char PORT6_5:1;
		unsigned char PORT6_6:1;
		unsigned char PORT6_7:1;		
	};
} __PORT6bits_t;
extern volatile __PORT6bits_t __at(PORT6_ADDR) PORT6bits;

#define PORT6_0         PORT6bits.PORT6_0   	/* bit 0 */
#define PORT6_1         PORT6bits.PORT6_1     	/* bit 1 */
#define PORT6_2         PORT6bits.PORT6_2       /* bit 2 */
#define PORT6_3         PORT6bits.PORT6_3       /* bit 3 */
#define PORT6_4         PORT6bits.PORT6_4   	/* bit 4 */
#define PORT6_5         PORT6bits.PORT6_5     	/* bit 5 */
#define PORT6_6         PORT6bits.PORT6_6       /* bit 6 */
#define PORT6_7         PORT6bits.PORT6_7       /* bit 7 */

// ----- LVDCON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char LVDCON_0:1;
		unsigned char LVDCON_1:1;
		unsigned char LVDCON_2:1;
		unsigned char LVDCON_3:1;	
		unsigned char LVDCON_4:1;
		unsigned char LVDCON_5:1;
		unsigned char LVDCON_6:1;
		unsigned char LVDCON_7:1;		
	};
} __LVDCONbits_t;
extern volatile __LVDCONbits_t __at(LVDCON_ADDR) LVDCONbits;

#define LVDSEL0			LVDCONbits.LVDCON_0   	/* bit 0 */
#define LVDSEL1			LVDCONbits.LVDCON_1     	/* bit 1 */
#define LVDSEL2			LVDCONbits.LVDCON_2       /* bit 2 */
#define LVDSEL3			LVDCONbits.LVDCON_3       /* bit 3 */
#define LVDSEL4			LVDCONbits.LVDCON_4   	/* bit 4 */
#define EXVEN			LVDCONbits.LVDCON_5     	/* bit 5 */
#define VDET			LVDCONbits.LVDCON_6       /* bit 6 */
#define LVDEN			LVDCONbits.LVDCON_7       /* bit 7 */

// ----- PWMCON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWMCON_0:1;
		unsigned char PWMCON_1:1;
		unsigned char PWMCON_2:1;
		unsigned char PWMCON_3:1;	
		unsigned char PWMCON_4:1;
		unsigned char PWMCON_5:1;
		unsigned char PWMCON_6:1;
		unsigned char PWMCON_7:1;		
	};
} __PWMCONbits_t;
extern volatile __PWMCONbits_t __at(PWMCON_ADDR) PWMCONbits;

#define T1PSR0			PWMCONbits.PWMCON_0   		/* bit 0 */
#define T1PSR1			PWMCONbits.PWMCON_1     	/* bit 1 */
#define T1PSR2			PWMCONbits.PWMCON_2       	/* bit 2 */
#define T1PTEN			PWMCONbits.PWMCON_3       	/* bit 3 */
#define PWM1EN			PWMCONbits.PWMCON_4   		/* bit 4 */
#define PWM2EN			PWMCONbits.PWMCON_5     	/* bit 5 */
#define PWM3EN			PWMCONbits.PWMCON_6       	/* bit 6 */
#define T1EN			PWMCONbits.PWMCON_7       	/* bit 7 */

// ----- PRD Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PRD_0:1;
		unsigned char PRD_1:1;
		unsigned char PRD_2:1;
		unsigned char PRD_3:1;	
		unsigned char PRD_4:1;
		unsigned char PRD_5:1;
		unsigned char PRD_6:1;
		unsigned char PRD_7:1;		
	};
} __PRDbits_t;
extern volatile __PRDbits_t __at(PRD_ADDR) PRDbits;

#define PRD_0         PRDbits.PRD_0   		/* bit 0 */
#define PRD_1         PRDbits.PRD_1    		/* bit 1 */
#define PRD_2         PRDbits.PRD_2    		/* bit 2 */
#define PRD_3         PRDbits.PRD_3    		/* bit 3 */
#define PRD_4         PRDbits.PRD_4   		/* bit 4 */
#define PRD_5         PRDbits.PRD_5    		/* bit 5 */
#define PRD_6         PRDbits.PRD_6    		/* bit 6 */
#define PRD_7         PRDbits.PRD_7    		/* bit 7 */

// ----- PDC1 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PDC1_0:1;
		unsigned char PDC1_1:1;
		unsigned char PDC1_2:1;
		unsigned char PDC1_3:1;	
		unsigned char PDC1_4:1;
		unsigned char PDC1_5:1;
		unsigned char PDC1_6:1;
		unsigned char PDC1_7:1;		
	};
} __PDC1bits_t;
extern volatile __PDC1bits_t __at(PDC1_ADDR) PDC1bits;

#define PDC1_0         PDC1bits.PDC1_0   	/* bit 0 */
#define PDC1_1         PDC1bits.PDC1_1     	/* bit 1 */
#define PDC1_2         PDC1bits.PDC1_2       	/* bit 2 */
#define PDC1_3         PDC1bits.PDC1_3       	/* bit 3 */
#define PDC1_4         PDC1bits.PDC1_4   	/* bit 4 */
#define PDC1_5         PDC1bits.PDC1_5     	/* bit 5 */
#define PDC1_6         PDC1bits.PDC1_6       	/* bit 6 */
#define PDC1_7         PDC1bits.PDC1_7       	/* bit 7 */

// ----- PDC2 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PDC2_0:1;
		unsigned char PDC2_1:1;
		unsigned char PDC2_2:1;
		unsigned char PDC2_3:1;	
		unsigned char PDC2_4:1;
		unsigned char PDC2_5:1;
		unsigned char PDC2_6:1;
		unsigned char PDC2_7:1;		
	};
} __PDC2bits_t;
extern volatile __PDC2bits_t __at(PDC2_ADDR) PDC2bits;

#define PDC2_0         PDC2bits.PDC2_0   	/* bit 0 */
#define PDC2_1         PDC2bits.PDC2_1     	/* bit 1 */
#define PDC2_2         PDC2bits.PDC2_2       	/* bit 2 */
#define PDC2_3         PDC2bits.PDC2_3       	/* bit 3 */
#define PDC2_4         PDC2bits.PDC2_4   	/* bit 4 */
#define PDC2_5         PDC2bits.PDC2_5     	/* bit 5 */
#define PDC2_6         PDC2bits.PDC2_6       	/* bit 6 */
#define PDC2_7         PDC2bits.PDC2_7       	/* bit 7 */

// ----- PDC3 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PDC3_0:1;
		unsigned char PDC3_1:1;
		unsigned char PDC3_2:1;
		unsigned char PDC3_3:1;	
		unsigned char PDC3_4:1;
		unsigned char PDC3_5:1;
		unsigned char PDC3_6:1;
		unsigned char PDC3_7:1;		
	};
} __PDC3bits_t;
extern volatile __PDC3bits_t __at(PDC3_ADDR) PDC3bits;

#define PDC3_0         PDC3bits.PDC3_0   	/* bit 0 */
#define PDC3_1         PDC3bits.PDC3_1     	/* bit 1 */
#define PDC3_2         PDC3bits.PDC3_2       	/* bit 2 */
#define PDC3_3         PDC3bits.PDC3_3       	/* bit 3 */
#define PDC3_4         PDC3bits.PDC3_4   	/* bit 4 */
#define PDC3_5         PDC3bits.PDC3_5     	/* bit 5 */
#define PDC3_6         PDC3bits.PDC3_6       	/* bit 6 */
#define PDC3_7         PDC3bits.PDC3_7       	/* bit 7 */

// ----- ICIECR Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ICIECR_0:1;
		unsigned char ICIECR_1:1;
		unsigned char ICIECR_2:1;
		unsigned char ICIECR_3:1;	
		unsigned char ICIECR_4:1;
		unsigned char ICIECR_5:1;
		unsigned char ICIECR_6:1;
		unsigned char ICIECR_7:1;		
	};
} __ICIECRbits_t;
extern volatile __ICIECRbits_t __at(ICIECR_ADDR) ICIECRbits;

#define IEN0		ICIECRbits.ICIECR_0   		/* bit 0 */
#define IEN1		ICIECRbits.ICIECR_1     	/* bit 1 */
#define IEN2		ICIECRbits.ICIECR_2       	/* bit 2 */
#define IEN3		ICIECRbits.ICIECR_3       	/* bit 3 */
#define IEN4		ICIECRbits.ICIECR_4   		/* bit 4 */
#define IEN5		ICIECRbits.ICIECR_5     	/* bit 5 */
#define IEN6        	ICIECRbits.ICIECR_6       	/* bit 6 */
#define IEN7        	ICIECRbits.ICIECR_7       	/* bit 7 */

// ----- CPUCON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char CPUCON_0:1;
		unsigned char CPUCON_1:1;
		unsigned char CPUCON_2:1;
		unsigned char CPUCON_3:1;	
		unsigned char CPUCON_4:1;
		unsigned char CPUCON_5:1;
		unsigned char CPUCON_6:1;
		unsigned char CPUCON_7:1;		
	};
} __CPUCONbits_t;
extern volatile __CPUCONbits_t __at(CPUCON_ADDR) CPUCONbits;

#define IDLE			CPUCONbits.CPUCON_0   	/* bit 0 */
#define CLKMD			CPUCONbits.CPUCON_1    /* bit 1 */
#define STPHX	        	CPUCONbits.CPUCON_2    /* bit 2 */
#define TCCWE			CPUCONbits.CPUCON_3    /* bit 3 */
#define PWMWE			CPUCONbits.CPUCON_4   	/* bit 4 */
#define TCCCKS			CPUCONbits.CPUCON_5    /* bit 5 */
#define PWMCKS			CPUCONbits.CPUCON_6    /* bit 6 */
#define IPWM1			CPUCONbits.CPUCON_7    /* bit 7 */

// ----- ISR Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ISR_0:1;
		unsigned char ISR_1:1;
		unsigned char ISR_2:1;
		unsigned char ISR_3:1;	
		unsigned char ISR_4:1;
		unsigned char ISR_5:1;
		unsigned char ISR_6:1;
		unsigned char ISR_7:1;		
	};
} __ISRbits_t;
extern volatile __ISRbits_t __at(ISR_ADDR) ISRbits;

#define TCIF         	ISRbits.ISR_0   		/* bit 0 */
#define ICIF         	ISRbits.ISR_1     		/* bit 1 */
#define EXIF         	ISRbits.ISR_2          		/* bit 2 */
#define T1IF         	ISRbits.ISR_3          		/* bit 3 */
#define ISR_4         	ISRbits.ISR_4   		/* bit 4 */
#define ISR_5         	ISRbits.ISR_5     		/* bit 5 */
#define ISR_6         	ISRbits.ISR_6          		/* bit 6 */
#define ISR_7         	ISRbits.ISR_7          		/* bit 7 */

#endif