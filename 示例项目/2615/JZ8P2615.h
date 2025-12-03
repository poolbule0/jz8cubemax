#ifndef __JZ8P2615_H__
#define __JZ8P2615_H__

//
// Register addresses.
//
#define RSR_ADDR			0X180
#define PCH_ADDR			0X181
#define PCL_ADDR			0X182
#define STATUS_ADDR			0X183
#define TC0CON_ADDR			0X184
#define TC0C_ADDR			0X185
#define TBRDH_ADDR			0X186
#define TBRDL_ADDR			0X187
#define CPUCON_ADDR			0X188
#define IHRCCAL_ADDR		0X189
#define PORT5_ADDR			0X18A
#define PORT6_ADDR			0X18B
#define P5CON_ADDR			0X18D
#define P6CON_ADDR			0X18E
                                        
#define P5PH_ADDR			0X190
#define P6PH_ADDR			0X191
#define P5PD_ADDR			0X193
#define P6PD_ADDR			0X194
#define P6OD_ADDR			0X199
#define P6WD_ADDR			0X19A
#define P5IWE_ADDR			0X19C
#define P6IWE_ADDR			0X19D
                                        
#define P5ADE_ADDR			0X1A0
#define P6ADE_ADDR			0X1A1
#define ADATH_ADDR			0X1A3
#define ADATL_ADDR			0X1A4
#define ADIS_ADDR			0X1A5
#define ADCON0_ADDR			0X1A6
#define ADCON1_ADDR			0X1A7
#define WDTCON_ADDR			0X1AF
                                        
#define TC1CON_ADDR			0X1B0
#define TC1PRDL_ADDR		0X1B1
#define PWM1DTL_ADDR		0X1B2
#define TC1PRDTH_ADDR		0X1B3
#define TC1CH_ADDR			0X1B4
#define TC1CL_ADDR			0X1B5
#define TC2CON_ADDR			0X1B6
#define TC2PRDL_ADDR		0X1B7
#define PWM2DTL_ADDR		0X1B8
#define TC2PRDTH_ADDR		0X1B9
#define TC2CH_ADDR			0X1BA
#define TC2CL_ADDR			0X1BB
#define PWM3DTH_ADDR		0X1BC
#define PWM3DTL_ADDR		0X1BD
#define PWM4DTH_ADDR		0X1BE
#define PWM4DTL_ADDR		0X1BF
                                        
#define PWMIS_ADDR			0X1C6
#define DEADCON_ADDR		0X1C7
#define PWMCON_ADDR			0X1C8
#define DEADT0_ADDR			0X1C9
#define DEADT1_ADDR			0X1CA
                                       
#define INTE0_ADDR			0X1D6
#define INTE1_ADDR			0X1D7
#define INTF0_ADDR			0X1DA
#define INTF1_ADDR			0X1DB
                                       
#define IAR_ADDR			0X1FF

//
//----- Register Files -----------------------------------------------------
//
extern __sfr __at (RSR_ADDR)	    RSR;	     	
extern __sfr __at (PCH_ADDR)	    PCH;	     	
extern __sfr __at (PCL_ADDR)	    PCL;	      	
extern __sfr __at (STATUS_ADDR)	    STATUS;	        	
extern __sfr __at (TC0CON_ADDR)	    TC0CON;	     	
extern __sfr __at (TC0C_ADDR)	    TC0C;	       	       	
extern __sfr __at (TBRDH_ADDR)	    TBRDH;	       	
extern __sfr __at (TBRDL_ADDR)	    TBRDL;	    	
extern __sfr __at (CPUCON_ADDR)	    CPUCON;	     	
extern __sfr __at (IHRCCAL_ADDR)	IHRCCAL;     	
extern __sfr __at (PORT5_ADDR)	    PORT5;	     	
extern __sfr __at (PORT6_ADDR)	    PORT6;	       	
extern __sfr __at (P5CON_ADDR)	    P5CON;	       	
extern __sfr __at (P6CON_ADDR)	    P6CON;	

extern __sfr __at (P5PH_ADDR)	    P5PH;	    	
extern __sfr __at (P6PH_ADDR)	    P6PH;	    	
extern __sfr __at (P5PD_ADDR)	    P5PD;	     	
extern __sfr __at (P6PD_ADDR)	    P6PD;	       	
extern __sfr __at (P6OD_ADDR)	    P6OD;	    	
extern __sfr __at (P6WD_ADDR)	    P6WD;	      
extern __sfr __at (P5IWE_ADDR)	    P5IWE;	      	
extern __sfr __at (P6IWE_ADDR)	    P6IWE;	   	
     	
extern __sfr __at (P5ADE_ADDR)	 	P5ADE;	    	
extern __sfr __at (P6ADE_ADDR)	 	P6ADE;	    	
extern __sfr __at (ADATH_ADDR)	 	ADATH;	     	
extern __sfr __at (ADATL_ADDR)	 	ADATL;	       	
extern __sfr __at (ADIS_ADDR)	 	ADIS;	    	
extern __sfr __at (ADCON0_ADDR)		ADCON0;	      
extern __sfr __at (ADCON1_ADDR)	 	ADCON1;	      	
extern __sfr __at (WDTCON_ADDR)	 	WDTCON;    	     	
     	
extern __sfr __at (TC1CON_ADDR)		TC1CON;	
extern __sfr __at (TC1PRDL_ADDR)	TC1PRDL;	        
extern __sfr __at (PWM1DTL_ADDR)	PWM1DTL;	        
extern __sfr __at (TC1PRDTH_ADDR)	TC1PRDTH;	
extern __sfr __at (TC1CH_ADDR)	    TC1CH;	        
extern __sfr __at (TC1CL_ADDR)	    TC1CL;	        
extern __sfr __at (TC2CON_ADDR)		TC2CON;        
extern __sfr __at (TC2PRDL_ADDR)	TC2PRDL;	        
extern __sfr __at (PWM2DTL_ADDR)	PWM2DTL;	        
extern __sfr __at (TC2PRDTH_ADDR)	TC2PRDTH;	    	
extern __sfr __at (TC2CH_ADDR)	    TC2CH;	        
extern __sfr __at (TC2CL_ADDR)	    TC2CL;	        
extern __sfr __at (PWM3DTH_ADDR)	PWM3DTH;	
extern __sfr __at (PWM3DTL_ADDR)	PWM3DTL;	
extern __sfr __at (PWM4DTH_ADDR)	PWM4DTH;	
extern __sfr __at (PWM4DTL_ADDR)	PWM4DTL;	

extern __sfr __at (PWMIS_ADDR)	 	PWMIS;	    	
extern __sfr __at (DEADCON_ADDR)	DEADCON;	    	
extern __sfr __at (PWMCON_ADDR)		PWMCON;	     	
extern __sfr __at (DEADT0_ADDR)	 	DEADT0;	       	
extern __sfr __at (DEADT1_ADDR)	 	DEADT1;

extern __sfr __at (INTE0_ADDR)	 	INTE0;	    	
extern __sfr __at (INTE1_ADDR)		INTE1;	    	
extern __sfr __at (INTF0_ADDR)		INTF0;	     	
extern __sfr __at (INTF1_ADDR)	 	INTF1;

extern __sfr __at (IAR_ADDR)	 	IAR;
 
//========================================================================
//	
//Configuration Bits
//	
//==========================================================================
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
#define RSR_1         	RSRbits.RSR_1     	/* bit 1 */
#define RSR_2         	RSRbits.RSR_2       /* bit 2 */
#define RSR_3         	RSRbits.RSR_3       /* bit 3 */
#define RSR_4         	RSRbits.RSR_4   	/* bit 4 */
#define RSR_5         	RSRbits.RSR_5     	/* bit 5 */
#define RSR_6         	RSRbits.RSR_6       /* bit 6 */
#define RSR_7         	RSRbits.RSR_7       /* bit 7 */

// ----- PCH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PCH_0:1;
		unsigned char PCH_1:1;
		unsigned char PCH_2:1;
		unsigned char PCH_3:1;	
		unsigned char PCH_4:1;
		unsigned char PCH_5:1;
		unsigned char PCH_6:1;
		unsigned char PCH_7:1;		
	};
} __PCHbits_t;
extern volatile __PCHbits_t __at(PCH_ADDR) PCHbits;

#define PCH_0         	PCHbits.PCH_0   	/* bit 0 */
#define PCH_1         	PCHbits.PCH_1     	/* bit 1 */
#define PCH_2         	PCHbits.PCH_2       /* bit 2 */
#define PCH_3         	PCHbits.PCH_3       /* bit 3 */
#define PCH_4         	PCHbits.PCH_4   	/* bit 4 */
#define PCH_5         	PCHbits.PCH_5     	/* bit 5 */
#define PCH_6         	PCHbits.PCH_6       /* bit 6 */
#define PCH_7         	PCHbits.PCH_7       /* bit 7 */

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

#define C         	STATUSbits.STATUS_0   		/* bit 0 */
#define DC         	STATUSbits.STATUS_1     	/* bit 1 */
#define Z         	STATUSbits.STATUS_2       	/* bit 2 */
#define P         	STATUSbits.STATUS_3       	/* bit 3 */
#define T         	STATUSbits.STATUS_4   		/* bit 4 */
#define GB0         STATUSbits.STATUS_5     	/* bit 5 */
#define GB1         STATUSbits.STATUS_6       	/* bit 6 */
#define RST         STATUSbits.STATUS_7       	/* bit 7 */

// ----- TC0CON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC0CON_0:1;
		unsigned char TC0CON_1:1;
		unsigned char TC0CON_2:1;
		unsigned char TC0CON_3:1;	
		unsigned char TC0CON_4:1;
		unsigned char TC0CON_5:1;
		unsigned char TC0CON_6:1;
		unsigned char TC0CON_7:1;		
	};
} __TC0CONbits_t;
extern volatile __TC0CONbits_t __at(TC0CON_ADDR) TC0CONbits;

#define TC0PSR0     TC0CONbits.TC0CON_0   		/* bit 0 */
#define TC0PSR1     TC0CONbits.TC0CON_1     	/* bit 1 */
#define TC0PSR2     TC0CONbits.TC0CON_2       	/* bit 2 */
#define PAB			TC0CONbits.TC0CON_3       	/* bit 3 */
#define TE         	TC0CONbits.TC0CON_4   		/* bit 4 */
#define TS         	TC0CONbits.TC0CON_5     	/* bit 5 */
#define GIE        TC0CONbits.TC0CON_6       	/* bit 6 */
#define TC0CKS      TC0CONbits.TC0CON_7       	/* bit 7 */

// ----- TC0C Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC0C_0:1;
		unsigned char TC0C_1:1;
		unsigned char TC0C_2:1;
		unsigned char TC0C_3:1;	
		unsigned char TC0C_4:1;
		unsigned char TC0C_5:1;
		unsigned char TC0C_6:1;
		unsigned char TC0C_7:1;		
	};
} __TC0Cbits_t;
extern volatile __TC0Cbits_t __at(TC0C_ADDR) TC0Cbits;

#define TC0C_0         	TC0Cbits.TC0C_0   		/* bit 0 */
#define TC0C_1         	TC0Cbits.TC0C_1     	/* bit 1 */
#define TC0C_2         	TC0Cbits.TC0C_2       	/* bit 2 */
#define TC0C_3         	TC0Cbits.TC0C_3       	/* bit 3 */
#define TC0C_4         	TC0Cbits.TC0C_4   		/* bit 4 */
#define TC0C_5         	TC0Cbits.TC0C_5     	/* bit 5 */
#define TC0C_6         	TC0Cbits.TC0C_6       	/* bit 6 */
#define TC0C_7         	TC0Cbits.TC0C_7       	/* bit 7 */

// ----- TBRDH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TBRDH_0:1;
		unsigned char TBRDH_1:1;
		unsigned char TBRDH_2:1;
		unsigned char TBRDH_3:1;	
		unsigned char TBRDH_4:1;
		unsigned char TBRDH_5:1;
		unsigned char TBRDH_6:1;
		unsigned char TBRDH_7:1;		
	};
} __TBRDHbits_t;
extern volatile __TBRDHbits_t __at(TBRDH_ADDR) TBRDHbits;

#define TBRDH_0         TBRDHbits.TBRDH_0   	/* bit 0 */
#define TBRDH_1         TBRDHbits.TBRDH_1     	/* bit 1 */
#define TBRDH_2         TBRDHbits.TBRDH_2       /* bit 2 */
#define TBRDH_3         TBRDHbits.TBRDH_3       /* bit 3 */
#define TBRDH_4         TBRDHbits.TBRDH_4   	/* bit 4 */
#define TBRDH_5         TBRDHbits.TBRDH_5     	/* bit 5 */
#define TBRDH_6         TBRDHbits.TBRDH_6       /* bit 6 */
#define TBRDH_7         TBRDHbits.TBRDH_7       /* bit 7 */

// ----- TBRDL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TBRDL_0:1;
		unsigned char TBRDL_1:1;
		unsigned char TBRDL_2:1;
		unsigned char TBRDL_3:1;	
		unsigned char TBRDL_4:1;
		unsigned char TBRDL_5:1;
		unsigned char TBRDL_6:1;
		unsigned char TBRDL_7:1;		
	};
} __TBRDLbits_t;
extern volatile __TBRDLbits_t __at(TBRDL_ADDR) TBRDLbits;

#define TBRDL_0         TBRDLbits.TBRDL_0   	/* bit 0 */
#define TBRDL_1         TBRDLbits.TBRDL_1     	/* bit 1 */
#define TBRDL_2         TBRDLbits.TBRDL_2       /* bit 2 */
#define TBRDL_3         TBRDLbits.TBRDL_3       /* bit 3 */
#define TBRDL_4         TBRDLbits.TBRDL_4   	/* bit 4 */
#define TBRDL_5         TBRDLbits.TBRDL_5     	/* bit 5 */
#define TBRDL_6         TBRDLbits.TBRDL_6      	/* bit 6 */
#define TBRDL_7         TBRDLbits.TBRDL_7       /* bit 7 */

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

#define IDLE         	CPUCONbits.CPUCON_0   	/* bit 0 */
#define CLKMD         	CPUCONbits.CPUCON_1     /* bit 1 */
#define STPHX         	CPUCONbits.CPUCON_2     /* bit 2 */
#define TC0WE         	CPUCONbits.CPUCON_3     /* bit 3 */
#define TC1WE         	CPUCONbits.CPUCON_4   	/* bit 4 */
#define ADCWE         	CPUCONbits.CPUCON_5     /* bit 5 */
#define INT0WE         	CPUCONbits.CPUCON_6     /* bit 6 */
#define INT1WE        	CPUCONbits.CPUCON_7     /* bit 7 */

// ----- IHRCCAL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char IHRCCAL_0:1;
		unsigned char IHRCCAL_1:1;
		unsigned char IHRCCAL_2:1;
		unsigned char IHRCCAL_3:1;	
		unsigned char IHRCCAL_4:1;
		unsigned char IHRCCAL_5:1;
		unsigned char IHRCCAL_6:1;
		unsigned char IHRCCAL_7:1;		
	};
} __IHRCCALbits_t;
extern volatile __IHRCCALbits_t __at(IHRCCAL_ADDR) IHRCCALbits;

#define IHRCCAL_0        IHRCCALbits.IHRCCAL_0   	/* bit 0 */
#define IHRCCAL_1        IHRCCALbits.IHRCCAL_1     	/* bit 1 */
#define IHRCCAL_2        IHRCCALbits.IHRCCAL_2      /* bit 2 */
#define IHRCCAL_3        IHRCCALbits.IHRCCAL_3      /* bit 3 */
#define IHRCCAL_4        IHRCCALbits.IHRCCAL_4   	/* bit 4 */
#define IHRCCAL_5        IHRCCALbits.IHRCCAL_5     	/* bit 5 */
#define IHRCCAL_6        IHRCCALbits.IHRCCAL_6      /* bit 6 */
#define IHRCCAL_7        IHRCCALbits.IHRCCAL_7      /* bit 7 */

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
#define PORT5_4         PORT5bits.PORT5_4   	/* bit 4 */
#define PORT5_5         PORT5bits.PORT5_5     	/* bit 5 */
#define PORT5_6         PORT5bits.PORT5_6       /* bit 6 */
#define PORT5_7         PORT5bits.PORT5_7       /* bit 7 */

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

// ----- P5CON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P5CON_0:1;
		unsigned char P5CON_1:1;
		unsigned char P5CON_2:1;
		unsigned char P5CON_3:1;	
		unsigned char P5CON_4:1;
		unsigned char P5CON_5:1;
		unsigned char P5CON_6:1;
		unsigned char P5CON_7:1;		
	};
} __P5CONbits_t;
extern volatile __P5CONbits_t __at(P5CON_ADDR) P5CONbits;

#define P5CON_0         P5CONbits.P5CON_0   	/* bit 0 */
#define P5CON_1         P5CONbits.P5CON_1     	/* bit 1 */
#define P5CON_2         P5CONbits.P5CON_2       /* bit 2 */
#define P5CON_3         P5CONbits.P5CON_3       /* bit 3 */
#define P5CON_4         P5CONbits.P5CON_4   	/* bit 4 */
#define P5CON_5         P5CONbits.P5CON_5     	/* bit 5 */
#define P5CON_6         P5CONbits.P5CON_6       /* bit 6 */
#define P5CON_7         P5CONbits.P5CON_7       /* bit 7 */

// ----- P6CON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6CON_0:1;
		unsigned char P6CON_1:1;
		unsigned char P6CON_2:1;
		unsigned char P6CON_3:1;	
		unsigned char P6CON_4:1;
		unsigned char P6CON_5:1;
		unsigned char P6CON_6:1;
		unsigned char P6CON_7:1;		
	};
} __P6CONbits_t;
extern volatile __P6CONbits_t __at(P6CON_ADDR) P6CONbits;

#define P6CON_0         P6CONbits.P6CON_0   	/* bit 0 */
#define P6CON_1         P6CONbits.P6CON_1     	/* bit 1 */
#define P6CON_2         P6CONbits.P6CON_2       /* bit 2 */
#define P6CON_3         P6CONbits.P6CON_3       /* bit 3 */
#define P6CON_4         P6CONbits.P6CON_4   	/* bit 4 */
#define P6CON_5         P6CONbits.P6CON_5     	/* bit 5 */
#define P6CON_6         P6CONbits.P6CON_6       /* bit 6 */
#define P6CON_7         P6CONbits.P6CON_7       /* bit 7 */

// ----- P5PH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P5PH_0:1;
		unsigned char P5PH_1:1;
		unsigned char P5PH_2:1;
		unsigned char P5PH_3:1;	
		unsigned char P5PH_4:1;
		unsigned char P5PH_5:1;
		unsigned char P5PH_6:1;
		unsigned char P5PH_7:1;		
	};
} __P5PHbits_t;
extern volatile __P5PHbits_t __at(P5PH_ADDR) P5PHbits;

#define P5PH_0         P5PHbits.P5PH_0   	/* bit 0 */
#define P5PH_1         P5PHbits.P5PH_1     	/* bit 1 */
#define P5PH_2         P5PHbits.P5PH_2      /* bit 2 */
#define P5PH_3         P5PHbits.P5PH_3      /* bit 3 */
#define P5PH_4         P5PHbits.P5PH_4   	/* bit 4 */
#define P5PH_5         P5PHbits.P5PH_5     	/* bit 5 */
#define P5PH_6         P5PHbits.P5PH_6      /* bit 6 */
#define P5PH_7         P5PHbits.P5PH_7      /* bit 7 */

// ----- P6PH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6PH_0:1;
		unsigned char P6PH_1:1;
		unsigned char P6PH_2:1;
		unsigned char P6PH_3:1;	
		unsigned char P6PH_4:1;
		unsigned char P6PH_5:1;
		unsigned char P6PH_6:1;
		unsigned char P6PH_7:1;		
	};
} __P6PHbits_t;
extern volatile __P6PHbits_t __at(P6PH_ADDR) P6PHbits;

#define P6PH_0         P6PHbits.P6PH_0   	/* bit 0 */
#define P6PH_1         P6PHbits.P6PH_1     	/* bit 1 */
#define P6PH_2         P6PHbits.P6PH_2      /* bit 2 */
#define P6PH_3         P6PHbits.P6PH_3      /* bit 3 */
#define P6PH_4         P6PHbits.P6PH_4   	/* bit 4 */
#define P6PH_5         P6PHbits.P6PH_5     	/* bit 5 */
#define P6PH_6         P6PHbits.P6PH_6      /* bit 6 */
#define P6PH_7         P6PHbits.P6PH_7      /* bit 7 */

// ----- P5PD Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P5PD_0:1;
		unsigned char P5PD_1:1;
		unsigned char P5PD_2:1;
		unsigned char P5PD_3:1;	
		unsigned char P5PD_4:1;
		unsigned char P5PD_5:1;
		unsigned char P5PD_6:1;
		unsigned char P5PD_7:1;		
	};
} __P5PDbits_t;
extern volatile __P5PDbits_t __at(P5PD_ADDR) P5PDbits;

#define P5PD_0         P5PDbits.P5PD_0   	/* bit 0 */
#define P5PD_1         P5PDbits.P5PD_1     	/* bit 1 */
#define P5PD_2         P5PDbits.P5PD_2      /* bit 2 */
#define P5PD_3         P5PDbits.P5PD_3      /* bit 3 */
#define P5PD_4         P5PDbits.P5PD_4   	/* bit 4 */
#define P5PD_5         P5PDbits.P5PD_5     	/* bit 5 */
#define P5PD_6         P5PDbits.P5PD_6      /* bit 6 */
#define P5PD_7         P5PDbits.P5PD_7      /* bit 7 */

// ----- P6PD Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6PD_0:1;
		unsigned char P6PD_1:1;
		unsigned char P6PD_2:1;
		unsigned char P6PD_3:1;	
		unsigned char P6PD_4:1;
		unsigned char P6PD_5:1;
		unsigned char P6PD_6:1;
		unsigned char P6PD_7:1;		
	};
} __P6PDbits_t;
extern volatile __P6PDbits_t __at(P6PD_ADDR) P6PDbits;

#define P6PD_0         P6PDbits.P6PD_0   	/* bit 0 */
#define P6PD_1         P6PDbits.P6PD_1     	/* bit 1 */
#define P6PD_2         P6PDbits.P6PD_2      /* bit 2 */
#define P6PD_3         P6PDbits.P6PD_3      /* bit 3 */
#define P6PD_4         P6PDbits.P6PD_4   	/* bit 4 */
#define P6PD_5         P6PDbits.P6PD_5     	/* bit 5 */
#define P6PD_6         P6PDbits.P6PD_6      /* bit 6 */
#define P6PD_7         P6PDbits.P6PD_7      /* bit 7 */

// ----- P6OD Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6OD_0:1;
		unsigned char P6OD_1:1;
		unsigned char P6OD_2:1;
		unsigned char P6OD_3:1;	
		unsigned char P6OD_4:1;
		unsigned char P6OD_5:1;
		unsigned char P6OD_6:1;
		unsigned char P6OD_7:1;		
	};
} __P6ODbits_t;
extern volatile __P6ODbits_t __at(P6OD_ADDR) P6ODbits;

#define P6OD_0         P6ODbits.P6OD_0   	/* bit 0 */
#define P6OD_1         P6ODbits.P6OD_1     	/* bit 1 */
#define P6OD_2         P6ODbits.P6OD_2      /* bit 2 */
#define P6OD_3         P6ODbits.P6OD_3      /* bit 3 */
#define P6OD_4         P6ODbits.P6OD_4   	/* bit 4 */
#define P6OD_5         P6ODbits.P6OD_5     	/* bit 5 */
#define P6OD_6         P6ODbits.P6OD_6      /* bit 6 */
#define P6OD_7         P6ODbits.P6OD_7      /* bit 7 */

// ----- P6WD Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6WD_0:1;
		unsigned char P6WD_1:1;
		unsigned char P6WD_2:1;
		unsigned char P6WD_3:1;	
		unsigned char P6WD_4:1;
		unsigned char P6WD_5:1;
		unsigned char P6WD_6:1;
		unsigned char P6WD_7:1;		
	};
} __P6WDbits_t;
extern volatile __P6WDbits_t __at(P6WD_ADDR) P6WDbits;

#define P6WD_0         P6WDbits.P6WD_0   	/* bit 0 */
#define P6WD_1         P6WDbits.P6WD_1     	/* bit 1 */
#define P6WD_2         P6WDbits.P6WD_2      /* bit 2 */
#define P6WD_3         P6WDbits.P6WD_3      /* bit 3 */
#define P6WD_4         P6WDbits.P6WD_4   	/* bit 4 */
#define P6WD_5         P6WDbits.P6WD_5     	/* bit 5 */
#define P6WD_6         P6WDbits.P6WD_6      /* bit 6 */
#define P6WD_7         P6WDbits.P6WD_7      /* bit 7 */

// ----- P5IWE Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P5IWE_0:1;
		unsigned char P5IWE_1:1;
		unsigned char P5IWE_2:1;
		unsigned char P5IWE_3:1;	
		unsigned char P5IWE_4:1;
		unsigned char P5IWE_5:1;
		unsigned char P5IWE_6:1;
		unsigned char P5IWE_7:1;		
	};
} __P5IWEbits_t;
extern volatile __P5IWEbits_t __at(P5IWE_ADDR) P5IWEbits;

#define P5IWE_0         P5IWEbits.P5IWE_0   	/* bit 0 */
#define P5IWE_1         P5IWEbits.P5IWE_1     	/* bit 1 */
#define P5IWE_2         P5IWEbits.P5IWE_2       /* bit 2 */
#define P5IWE_3         P5IWEbits.P5IWE_3       /* bit 3 */
#define P5IWE_4         P5IWEbits.P5IWE_4   	/* bit 4 */
#define P5IWE_5         P5IWEbits.P5IWE_5     	/* bit 5 */
#define P5IWE_6         P5IWEbits.P5IWE_6       /* bit 6 */
#define P5IWE_7         P5IWEbits.P5IWE_7       /* bit 7 */

// ----- P6IWE Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6IWE_0:1;
		unsigned char P6IWE_1:1;
		unsigned char P6IWE_2:1;
		unsigned char P6IWE_3:1;	
		unsigned char P6IWE_4:1;
		unsigned char P6IWE_5:1;
		unsigned char P6IWE_6:1;
		unsigned char P6IWE_7:1;		
	};
} __P6IWEbits_t;
extern volatile __P6IWEbits_t __at(P6IWE_ADDR) P6IWEbits;

#define P6IWE_0         P6IWEbits.P6IWE_0   	/* bit 0 */
#define P6IWE_1         P6IWEbits.P6IWE_1     	/* bit 1 */
#define P6IWE_2         P6IWEbits.P6IWE_2       /* bit 2 */
#define P6IWE_3         P6IWEbits.P6IWE_3       /* bit 3 */
#define P6IWE_4         P6IWEbits.P6IWE_4   	/* bit 4 */
#define P6IWE_5         P6IWEbits.P6IWE_5     	/* bit 5 */
#define P6IWE_6         P6IWEbits.P6IWE_6       /* bit 6 */
#define P6IWE_7         P6IWEbits.P6IWE_7       /* bit 7 */

// ----- P5ADE Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P5ADE_0:1;
		unsigned char P5ADE_1:1;
		unsigned char P5ADE_2:1;
		unsigned char P5ADE_3:1;	
		unsigned char P5ADE_4:1;
		unsigned char P5ADE_5:1;
		unsigned char P5ADE_6:1;
		unsigned char P5ADE_7:1;		
	};
} __P5ADEbits_t;
extern volatile __P5ADEbits_t __at(P5ADE_ADDR) P5ADEbits;

#define P5ADE_0         P5ADEbits.P5ADE_0   	/* bit 0 */
#define P5ADE_1         P5ADEbits.P5ADE_1     	/* bit 1 */
#define P5ADE_2         P5ADEbits.P5ADE_2       /* bit 2 */
#define P5ADE_3         P5ADEbits.P5ADE_3       /* bit 3 */
#define P5ADE_4         P5ADEbits.P5ADE_4   	/* bit 4 */
#define P5ADE_5         P5ADEbits.P5ADE_5     	/* bit 5 */
#define P5ADE_6         P5ADEbits.P5ADE_6       /* bit 6 */
#define P5ADE_7         P5ADEbits.P5ADE_7       /* bit 7 */

// ----- P6ADE Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char P6ADE_0:1;
		unsigned char P6ADE_1:1;
		unsigned char P6ADE_2:1;
		unsigned char P6ADE_3:1;	
		unsigned char P6ADE_4:1;
		unsigned char P6ADE_5:1;
		unsigned char P6ADE_6:1;
		unsigned char P6ADE_7:1;		
	};
} __P6ADEbits_t;
extern volatile __P6ADEbits_t __at(P6ADE_ADDR) P6ADEbits;

#define P6ADE_0         P6ADEbits.P6ADE_0   	/* bit 0 */
#define P6ADE_1         P6ADEbits.P6ADE_1     	/* bit 1 */
#define P6ADE_2         P6ADEbits.P6ADE_2       /* bit 2 */
#define P6ADE_3         P6ADEbits.P6ADE_3       /* bit 3 */
#define P6ADE_4         P6ADEbits.P6ADE_4   	/* bit 4 */
#define P6ADE_5         P6ADEbits.P6ADE_5     	/* bit 5 */
#define P6ADE_6         P6ADEbits.P6ADE_6       /* bit 6 */
#define P6ADE_7         P6ADEbits.P6ADE_7       /* bit 7 */

// ----- ADATH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ADATH_0:1;
		unsigned char ADATH_1:1;
		unsigned char ADATH_2:1;
		unsigned char ADATH_3:1;	
		unsigned char ADATH_4:1;
		unsigned char ADATH_5:1;
		unsigned char ADATH_6:1;
		unsigned char ADATH_7:1;		
	};
} __ADATHbits_t;
extern volatile __ADATHbits_t __at(ADATH_ADDR) ADATHbits;

#define ADATH_0         ADATHbits.ADATH_0   	/* bit 0 */
#define ADATH_1         ADATHbits.ADATH_1     	/* bit 1 */
#define ADATH_2         ADATHbits.ADATH_2       /* bit 2 */
#define ADATH_3         ADATHbits.ADATH_3       /* bit 3 */
#define ADATH_4         ADATHbits.ADATH_4   	/* bit 4 */
#define ADATH_5         ADATHbits.ADATH_5     	/* bit 5 */
#define ADATH_6         ADATHbits.ADATH_6       /* bit 6 */
#define ADATH_7         ADATHbits.ADATH_7       /* bit 7 */

// ----- ADATL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ADATL_0:1;
		unsigned char ADATL_1:1;
		unsigned char ADATL_2:1;
		unsigned char ADATL_3:1;	
		unsigned char ADATL_4:1;
		unsigned char ADATL_5:1;
		unsigned char ADATL_6:1;
		unsigned char ADATL_7:1;		
	};
} __ADATLbits_t;
extern volatile __ADATLbits_t __at(ADATL_ADDR) ADATLbits;

#define ADATL_0         ADATLbits.ADATL_0   	/* bit 0 */
#define ADATL_1         ADATLbits.ADATL_1     	/* bit 1 */
#define ADATL_2         ADATLbits.ADATL_2       /* bit 2 */
#define ADATL_3         ADATLbits.ADATL_3       /* bit 3 */
#define ADATL_4         ADATLbits.ADATL_4   	/* bit 4 */
#define ADATL_5         ADATLbits.ADATL_5     	/* bit 5 */
#define ADATL_6         ADATLbits.ADATL_6       /* bit 6 */
#define ADATL_7         ADATLbits.ADATL_7       /* bit 7 */

// ----- ADIS Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ADIS_0:1;
		unsigned char ADIS_1:1;
		unsigned char ADIS_2:1;
		unsigned char ADIS_3:1;	
		unsigned char ADIS_4:1;
		unsigned char ADIS_5:1;
		unsigned char ADIS_6:1;
		unsigned char ADIS_7:1;		
	};
} __ADISbits_t;
extern volatile __ADISbits_t __at(ADIS_ADDR) ADISbits;

#define ADAT_8         	ADISbits.ADIS_0   		/* bit 0 */
#define ADAT_9         	ADISbits.ADIS_1			/* bit 1 */
#define ADAT_10         ADISbits.ADIS_2			/* bit 2 */
#define ADAT_11         ADISbits.ADIS_3			/* bit 3 */
#define ADIS0         	ADISbits.ADIS_4   		/* bit 4 */
#define ADIS1         	ADISbits.ADIS_5     	/* bit 5 */
#define ADIS2         	ADISbits.ADIS_6       	/* bit 6 */
#define ADIS3         	ADISbits.ADIS_7       	/* bit 7 */

// ----- ADCON0 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ADCON0_0:1;
		unsigned char ADCON0_1:1;
		unsigned char ADCON0_2:1;
		unsigned char ADCON0_3:1;	
		unsigned char ADCON0_4:1;
		unsigned char ADCON0_5:1;
		unsigned char ADCON0_6:1;
		unsigned char ADCON0_7:1;		
	};
} __ADCON0bits_t;
extern volatile __ADCON0bits_t __at(ADCON0_ADDR) ADCON0bits;

#define VREF0         	ADCON0bits.ADCON0_0   		/* bit 0 */
#define VREF1         	ADCON0bits.ADCON0_1     	/* bit 1 */
#define VREF2         	ADCON0bits.ADCON0_2       	/* bit 2 */
#define ADCON0_3        ADCON0bits.ADCON0_3       	/* bit 3 */
#define ADCON0_4        ADCON0bits.ADCON0_4   		/* bit 4 */
#define ADCON0_5        ADCON0bits.ADCON0_5     	/* bit 5 */
#define ADPSR0         	ADCON0bits.ADCON0_6       	/* bit 6 */
#define ADPSR1         	ADCON0bits.ADCON0_7       	/* bit 7 */

// ----- ADCON1 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char ADCON1_0:1;
		unsigned char ADCON1_1:1;
		unsigned char ADCON1_2:1;
		unsigned char ADCON1_3:1;	
		unsigned char ADCON1_4:1;
		unsigned char ADCON1_5:1;
		unsigned char ADCON1_6:1;
		unsigned char ADCON1_7:1;		
	};
} __ADCON1bits_t;
extern volatile __ADCON1bits_t __at(ADCON1_ADDR) ADCON1bits;

#define VOF0         	ADCON1bits.ADCON1_0   		/* bit 0 */
#define VOF1         	ADCON1bits.ADCON1_1     	/* bit 1 */
#define VOF2         	ADCON1bits.ADCON1_2       	/* bit 2 */
#define SIGN         	ADCON1bits.ADCON1_3       	/* bit 3 */
#define CALI         	ADCON1bits.ADCON1_4   		/* bit 4 */
#define VREFS         	ADCON1bits.ADCON1_5     	/* bit 5 */
#define ADEN         	ADCON1bits.ADCON1_6       	/* bit 6 */
#define ADRUN         	ADCON1bits.ADCON1_7       	/* bit 7 */

// ----- WDTCON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char WDTCON_0:1;
		unsigned char WDTCON_1:1;
		unsigned char WDTCON_2:1;
		unsigned char WDTCON_3:1;	
		unsigned char WDTCON_4:1;
		unsigned char WDTCON_5:1;
		unsigned char WDTCON_6:1;
		unsigned char WDTCON_7:1;		
	};
} __WDTCONbits_t;
extern volatile __WDTCONbits_t __at(WDTCON_ADDR) WDTCONbits;

#define WDTCON_0        WDTCONbits.WDTCON_0   		/* bit 0 */
#define WDTCON_1        WDTCONbits.WDTCON_1     	/* bit 1 */
#define INT0EDG         WDTCONbits.WDTCON_2       	/* bit 2 */
#define INT1EDG         WDTCONbits.WDTCON_3       	/* bit 3 */
#define VFOE         	WDTCONbits.WDTCON_4   		/* bit 4 */
#define INT1EN         	WDTCONbits.WDTCON_5     	/* bit 5 */
#define INT0EN         	WDTCONbits.WDTCON_6       	/* bit 6 */
#define WDTE         	WDTCONbits.WDTCON_7       	/* bit 7 */

// ----- TC1CON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC1CON_0:1;
		unsigned char TC1CON_1:1;
		unsigned char TC1CON_2:1;
		unsigned char TC1CON_3:1;	
		unsigned char TC1CON_4:1;
		unsigned char TC1CON_5:1;
		unsigned char TC1CON_6:1;
		unsigned char TC1CON_7:1;		
	};
} __TC1CONbits_t;
extern volatile __TC1CONbits_t __at(TC1CON_ADDR) TC1CONbits;

#define TC1PSR0         TC1CONbits.TC1CON_0   		/* bit 0 */
#define TC1PSR1         TC1CONbits.TC1CON_1     	/* bit 1 */
#define TC1PSR2         TC1CONbits.TC1CON_2       	/* bit 2 */
#define PWM1E         	TC1CONbits.TC1CON_3       	/* bit 3 */
#define IPWM1E         	TC1CONbits.TC1CON_4   		/* bit 4 */
#define PWM3E         	TC1CONbits.TC1CON_5     	/* bit 5 */
#define IPWM3E         	TC1CONbits.TC1CON_6       	/* bit 6 */
#define TC1EN         	TC1CONbits.TC1CON_7       	/* bit 7 */

// ----- TC1PRDL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC1PRDL_0:1;
		unsigned char TC1PRDL_1:1;
		unsigned char TC1PRDL_2:1;
		unsigned char TC1PRDL_3:1;	
		unsigned char TC1PRDL_4:1;
		unsigned char TC1PRDL_5:1;
		unsigned char TC1PRDL_6:1;
		unsigned char TC1PRDL_7:1;		
	};
} __TC1PRDLbits_t;
extern volatile __TC1PRDLbits_t __at(TC1PRDL_ADDR) TC1PRDLbits;

#define TC1PRDL_0         TC1PRDLbits.TC1PRDL_0   		/* bit 0 */
#define TC1PRDL_1         TC1PRDLbits.TC1PRDL_1     	/* bit 1 */
#define TC1PRDL_2         TC1PRDLbits.TC1PRDL_2       	/* bit 2 */
#define TC1PRDL_3         TC1PRDLbits.TC1PRDL_3       	/* bit 3 */
#define TC1PRDL_4         TC1PRDLbits.TC1PRDL_4   		/* bit 4 */
#define TC1PRDL_5         TC1PRDLbits.TC1PRDL_5     	/* bit 5 */
#define TC1PRDL_6         TC1PRDLbits.TC1PRDL_6       	/* bit 6 */
#define TC1PRDL_7         TC1PRDLbits.TC1PRDL_7       	/* bit 7 */

// ----- PWM1DTL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWM1DTL_0:1;
		unsigned char PWM1DTL_1:1;
		unsigned char PWM1DTL_2:1;
		unsigned char PWM1DTL_3:1;	
		unsigned char PWM1DTL_4:1;
		unsigned char PWM1DTL_5:1;
		unsigned char PWM1DTL_6:1;
		unsigned char PWM1DTL_7:1;		
	};
} __PWM1DTLbits_t;
extern volatile __PWM1DTLbits_t __at(PWM1DTL_ADDR) PWM1DTLbits;

#define PWM1DTL_0         PWM1DTLbits.PWM1DTL_0   		/* bit 0 */
#define PWM1DTL_1         PWM1DTLbits.PWM1DTL_1     	/* bit 1 */
#define PWM1DTL_2         PWM1DTLbits.PWM1DTL_2       	/* bit 2 */
#define PWM1DTL_3         PWM1DTLbits.PWM1DTL_3       	/* bit 3 */
#define PWM1DTL_4         PWM1DTLbits.PWM1DTL_4   		/* bit 4 */
#define PWM1DTL_5         PWM1DTLbits.PWM1DTL_5     	/* bit 5 */
#define PWM1DTL_6         PWM1DTLbits.PWM1DTL_6       	/* bit 6 */
#define PWM1DTL_7         PWM1DTLbits.PWM1DTL_7       	/* bit 7 */

// ----- TC1PRDTH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC1PRDTH_0:1;
		unsigned char TC1PRDTH_1:1;
		unsigned char TC1PRDTH_2:1;
		unsigned char TC1PRDTH_3:1;	
		unsigned char TC1PRDTH_4:1;
		unsigned char TC1PRDTH_5:1;
		unsigned char TC1PRDTH_6:1;
		unsigned char TC1PRDTH_7:1;		
	};
} __TC1PRDTHbits_t;
extern volatile __TC1PRDTHbits_t __at(TC1PRDTH_ADDR) TC1PRDTHbits;

#define TC1PRDTH_0         TC1PRDTHbits.TC1PRDTH_0   		/* bit 0 */
#define TC1PRDTH_1         TC1PRDTHbits.TC1PRDTH_1     		/* bit 1 */
#define TC1PRDTH_2         TC1PRDTHbits.TC1PRDTH_2       	/* bit 2 */
#define TC1PRDTH_3         TC1PRDTHbits.TC1PRDTH_3       	/* bit 3 */
#define TC1PRDTH_4         TC1PRDTHbits.TC1PRDTH_4   		/* bit 4 */
#define TC1PRDTH_5         TC1PRDTHbits.TC1PRDTH_5     		/* bit 5 */
#define TC1PRDTH_6         TC1PRDTHbits.TC1PRDTH_6       	/* bit 6 */
#define TC1PRDTH_7         TC1PRDTHbits.TC1PRDTH_7       	/* bit 7 */

// ----- TC1CH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC1CH_0:1;
		unsigned char TC1CH_1:1;
		unsigned char TC1CH_2:1;
		unsigned char TC1CH_3:1;	
		unsigned char TC1CH_4:1;
		unsigned char TC1CH_5:1;
		unsigned char TC1CH_6:1;
		unsigned char TC1CH_7:1;		
	};
} __TC1CHbits_t;
extern volatile __TC1CHbits_t __at(TC1CH_ADDR) TC1CHbits;

#define TC1CH_0         TC1CHbits.TC1CH_0   		/* bit 0 */
#define TC1CH_1         TC1CHbits.TC1CH_1     		/* bit 1 */
#define TC1CH_2         TC1CHbits.TC1CH_2       	/* bit 2 */
#define TC1CH_3         TC1CHbits.TC1CH_3       	/* bit 3 */
#define TC1CH_4         TC1CHbits.TC1CH_4   		/* bit 4 */
#define TC1CH_5         TC1CHbits.TC1CH_5     		/* bit 5 */
#define TC1CH_6         TC1CHbits.TC1CH_6       	/* bit 6 */
#define TC1CH_7         TC1CHbits.TC1CH_7       	/* bit 7 */

// ----- TC1CL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC1CL_0:1;
		unsigned char TC1CL_1:1;
		unsigned char TC1CL_2:1;
		unsigned char TC1CL_3:1;	
		unsigned char TC1CL_4:1;
		unsigned char TC1CL_5:1;
		unsigned char TC1CL_6:1;
		unsigned char TC1CL_7:1;		
	};
} __TC1CLbits_t;
extern volatile __TC1CLbits_t __at(TC1CL_ADDR) TC1CLbits;

#define TC1CL_0         TC1CLbits.TC1CL_0   		/* bit 0 */
#define TC1CL_1         TC1CLbits.TC1CL_1     		/* bit 1 */
#define TC1CL_2         TC1CLbits.TC1CL_2       	/* bit 2 */
#define TC1CL_3         TC1CLbits.TC1CL_3       	/* bit 3 */
#define TC1CL_4         TC1CLbits.TC1CL_4   		/* bit 4 */
#define TC1CL_5         TC1CLbits.TC1CL_5     		/* bit 5 */
#define TC1CL_6         TC1CLbits.TC1CL_6       	/* bit 6 */
#define TC1CL_7         TC1CLbits.TC1CL_7       	/* bit 7 */

// ----- TC2CON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC2CON_0:1;
		unsigned char TC2CON_1:1;
		unsigned char TC2CON_2:1;
		unsigned char TC2CON_3:1;	
		unsigned char TC2CON_4:1;
		unsigned char TC2CON_5:1;
		unsigned char TC2CON_6:1;
		unsigned char TC2CON_7:1;		
	};
} __TC2CONbits_t;
extern volatile __TC2CONbits_t __at(TC2CON_ADDR) TC2CONbits;

#define TC2PSR0         TC2CONbits.TC2CON_0   		/* bit 0 */
#define TC2PSR1         TC2CONbits.TC2CON_1     	/* bit 1 */
#define TC2PSR2         TC2CONbits.TC2CON_2       	/* bit 2 */
#define PWM2E         	TC2CONbits.TC2CON_3       	/* bit 3 */
#define IPWM2E         	TC2CONbits.TC2CON_4   		/* bit 4 */
#define PWM4E         	TC2CONbits.TC2CON_5     	/* bit 5 */
#define IPWM4E         	TC2CONbits.TC2CON_6       	/* bit 6 */
#define TC2EN         	TC2CONbits.TC2CON_7       	/* bit 7 */

// ----- TC2PRDL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC2PRDL_0:1;
		unsigned char TC2PRDL_1:1;
		unsigned char TC2PRDL_2:1;
		unsigned char TC2PRDL_3:1;	
		unsigned char TC2PRDL_4:1;
		unsigned char TC2PRDL_5:1;
		unsigned char TC2PRDL_6:1;
		unsigned char TC2PRDL_7:1;		
	};
} __TC2PRDLbits_t;
extern volatile __TC2PRDLbits_t __at(TC2PRDL_ADDR) TC2PRDLbits;

#define TC2PRDL_0         TC2PRDLbits.TC2PRDL_0   		/* bit 0 */
#define TC2PRDL_1         TC2PRDLbits.TC2PRDL_1     	/* bit 1 */
#define TC2PRDL_2         TC2PRDLbits.TC2PRDL_2       	/* bit 2 */
#define TC2PRDL_3         TC2PRDLbits.TC2PRDL_3       	/* bit 3 */
#define TC2PRDL_4         TC2PRDLbits.TC2PRDL_4   		/* bit 4 */
#define TC2PRDL_5         TC2PRDLbits.TC2PRDL_5     	/* bit 5 */
#define TC2PRDL_6         TC2PRDLbits.TC2PRDL_6       	/* bit 6 */
#define TC2PRDL_7         TC2PRDLbits.TC2PRDL_7       	/* bit 7 */

// ----- PWM2DTL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWM2DTL_0:1;
		unsigned char PWM2DTL_1:1;
		unsigned char PWM2DTL_2:1;
		unsigned char PWM2DTL_3:1;	
		unsigned char PWM2DTL_4:1;
		unsigned char PWM2DTL_5:1;
		unsigned char PWM2DTL_6:1;
		unsigned char PWM2DTL_7:1;		
	};
} __PWM2DTLbits_t;
extern volatile __PWM2DTLbits_t __at(PWM2DTL_ADDR) PWM2DTLbits;

#define PWM2DTL_0         PWM2DTLbits.PWM2DTL_0   		/* bit 0 */
#define PWM2DTL_1         PWM2DTLbits.PWM2DTL_1     	/* bit 1 */
#define PWM2DTL_2         PWM2DTLbits.PWM2DTL_2       	/* bit 2 */
#define PWM2DTL_3         PWM2DTLbits.PWM2DTL_3       	/* bit 3 */
#define PWM2DTL_4         PWM2DTLbits.PWM2DTL_4   		/* bit 4 */
#define PWM2DTL_5         PWM2DTLbits.PWM2DTL_5     	/* bit 5 */
#define PWM2DTL_6         PWM2DTLbits.PWM2DTL_6       	/* bit 6 */
#define PWM2DTL_7         PWM2DTLbits.PWM2DTL_7       	/* bit 7 */

// ----- TC2PRDTH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC2PRDTH_0:1;
		unsigned char TC2PRDTH_1:1;
		unsigned char TC2PRDTH_2:1;
		unsigned char TC2PRDTH_3:1;	
		unsigned char TC2PRDTH_4:1;
		unsigned char TC2PRDTH_5:1;
		unsigned char TC2PRDTH_6:1;
		unsigned char TC2PRDTH_7:1;		
	};
} __TC2PRDTHbits_t;
extern volatile __TC2PRDTHbits_t __at(TC2PRDTH_ADDR) TC2PRDTHbits;

#define TC2PRDTH_0         TC2PRDTHbits.TC2PRDTH_0   		/* bit 0 */
#define TC2PRDTH_1         TC2PRDTHbits.TC2PRDTH_1     		/* bit 1 */
#define TC2PRDTH_2         TC2PRDTHbits.TC2PRDTH_2       	/* bit 2 */
#define TC2PRDTH_3         TC2PRDTHbits.TC2PRDTH_3       	/* bit 3 */
#define TC2PRDTH_4         TC2PRDTHbits.TC2PRDTH_4   		/* bit 4 */
#define TC2PRDTH_5         TC2PRDTHbits.TC2PRDTH_5     		/* bit 5 */
#define TC2PRDTH_6         TC2PRDTHbits.TC2PRDTH_6       	/* bit 6 */
#define TC2PRDTH_7         TC2PRDTHbits.TC2PRDTH_7       	/* bit 7 */

// ----- TC2CH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC2CH_0:1;
		unsigned char TC2CH_1:1;
		unsigned char TC2CH_2:1;
		unsigned char TC2CH_3:1;	
		unsigned char TC2CH_4:1;
		unsigned char TC2CH_5:1;
		unsigned char TC2CH_6:1;
		unsigned char TC2CH_7:1;		
	};
} __TC2CHbits_t;
extern volatile __TC2CHbits_t __at(TC2CH_ADDR) TC2CHbits;

#define TC2CH_0         TC2CHbits.TC2CH_0   		/* bit 0 */
#define TC2CH_1         TC2CHbits.TC2CH_1     		/* bit 1 */
#define TC2CH_2         TC2CHbits.TC2CH_2       	/* bit 2 */
#define TC2CH_3         TC2CHbits.TC2CH_3       	/* bit 3 */
#define TC2CH_4         TC2CHbits.TC2CH_4   		/* bit 4 */
#define TC2CH_5         TC2CHbits.TC2CH_5     		/* bit 5 */
#define TC2CH_6         TC2CHbits.TC2CH_6       	/* bit 6 */
#define TC2CH_7         TC2CHbits.TC2CH_7       	/* bit 7 */

// ----- TC2CL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char TC2CL_0:1;
		unsigned char TC2CL_1:1;
		unsigned char TC2CL_2:1;
		unsigned char TC2CL_3:1;	
		unsigned char TC2CL_4:1;
		unsigned char TC2CL_5:1;
		unsigned char TC2CL_6:1;
		unsigned char TC2CL_7:1;		
	};
} __TC2CLbits_t;
extern volatile __TC2CLbits_t __at(TC2CL_ADDR) TC2CLbits;

#define TC2CL_0         TC2CLbits.TC2CL_0   		/* bit 0 */
#define TC2CL_1         TC2CLbits.TC2CL_1     		/* bit 1 */
#define TC2CL_2         TC2CLbits.TC2CL_2       	/* bit 2 */
#define TC2CL_3         TC2CLbits.TC2CL_3       	/* bit 3 */
#define TC2CL_4         TC2CLbits.TC2CL_4   		/* bit 4 */
#define TC2CL_5         TC2CLbits.TC2CL_5     		/* bit 5 */
#define TC2CL_6         TC2CLbits.TC2CL_6       	/* bit 6 */
#define TC2CL_7         TC2CLbits.TC2CL_7       	/* bit 7 */

// ----- PWM3DTH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWM3DTH_0:1;
		unsigned char PWM3DTH_1:1;
		unsigned char PWM3DTH_2:1;
		unsigned char PWM3DTH_3:1;	
		unsigned char PWM3DTH_4:1;
		unsigned char PWM3DTH_5:1;
		unsigned char PWM3DTH_6:1;
		unsigned char PWM3DTH_7:1;		
	};
} __PWM3DTHbits_t;
extern volatile __PWM3DTHbits_t __at(PWM3DTH_ADDR) PWM3DTHbits;

#define PWM3DTH_0         PWM3DTHbits.PWM3DTH_0   		/* bit 0 */
#define PWM3DTH_1         PWM3DTHbits.PWM3DTH_1     	/* bit 1 */
#define PWM3DTH_2         PWM3DTHbits.PWM3DTH_2       	/* bit 2 */
#define PWM3DTH_3         PWM3DTHbits.PWM3DTH_3       	/* bit 3 */
#define PWM3DTH_4         PWM3DTHbits.PWM3DTH_4   		/* bit 4 */
#define PWM3DTH_5         PWM3DTHbits.PWM3DTH_5     	/* bit 5 */
#define PWM3DTH_6         PWM3DTHbits.PWM3DTH_6       	/* bit 6 */
#define PWM3DTH_7         PWM3DTHbits.PWM3DTH_7       	/* bit 7 */

// ----- PWM3DTL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWM3DTL_0:1;
		unsigned char PWM3DTL_1:1;
		unsigned char PWM3DTL_2:1;
		unsigned char PWM3DTL_3:1;	
		unsigned char PWM3DTL_4:1;
		unsigned char PWM3DTL_5:1;
		unsigned char PWM3DTL_6:1;
		unsigned char PWM3DTL_7:1;		
	};
} __PWM3DTLbits_t;
extern volatile __PWM3DTLbits_t __at(PWM3DTL_ADDR) PWM3DTLbits;

#define PWM3DTL_0         PWM3DTLbits.PWM3DTL_0   		/* bit 0 */
#define PWM3DTL_1         PWM3DTLbits.PWM3DTL_1     	/* bit 1 */
#define PWM3DTL_2         PWM3DTLbits.PWM3DTL_2       	/* bit 2 */
#define PWM3DTL_3         PWM3DTLbits.PWM3DTL_3       	/* bit 3 */
#define PWM3DTL_4         PWM3DTLbits.PWM3DTL_4   		/* bit 4 */
#define PWM3DTL_5         PWM3DTLbits.PWM3DTL_5     	/* bit 5 */
#define PWM3DTL_6         PWM3DTLbits.PWM3DTL_6       	/* bit 6 */
#define PWM3DTL_7         PWM3DTLbits.PWM3DTL_7       	/* bit 7 */

// ----- PWM4DTH Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWM4DTH_0:1;
		unsigned char PWM4DTH_1:1;
		unsigned char PWM4DTH_2:1;
		unsigned char PWM4DTH_3:1;	
		unsigned char PWM4DTH_4:1;
		unsigned char PWM4DTH_5:1;
		unsigned char PWM4DTH_6:1;
		unsigned char PWM4DTH_7:1;		
	};
} __PWM4DTHbits_t;
extern volatile __PWM4DTHbits_t __at(PWM4DTH_ADDR) PWM4DTHbits;

#define PWM4DTH_0         PWM4DTHbits.PWM4DTH_0   		/* bit 0 */
#define PWM4DTH_1         PWM4DTHbits.PWM4DTH_1     	/* bit 1 */
#define PWM4DTH_2         PWM4DTHbits.PWM4DTH_2       	/* bit 2 */
#define PWM4DTH_3         PWM4DTHbits.PWM4DTH_3       	/* bit 3 */
#define PWM4DTH_4         PWM4DTHbits.PWM4DTH_4   		/* bit 4 */
#define PWM4DTH_5         PWM4DTHbits.PWM4DTH_5     	/* bit 5 */
#define PWM4DTH_6         PWM4DTHbits.PWM4DTH_6       	/* bit 6 */
#define PWM4DTH_7         PWM4DTHbits.PWM4DTH_7       	/* bit 7 */

// ----- PWM4DTL Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWM4DTL_0:1;
		unsigned char PWM4DTL_1:1;
		unsigned char PWM4DTL_2:1;
		unsigned char PWM4DTL_3:1;	
		unsigned char PWM4DTL_4:1;
		unsigned char PWM4DTL_5:1;
		unsigned char PWM4DTL_6:1;
		unsigned char PWM4DTL_7:1;		
	};
} __PWM4DTLbits_t;
extern volatile __PWM4DTLbits_t __at(PWM4DTL_ADDR) PWM4DTLbits;

#define PWM4DTL_0         PWM4DTLbits.PWM4DTL_0   		/* bit 0 */
#define PWM4DTL_1         PWM4DTLbits.PWM4DTL_1     	/* bit 1 */
#define PWM4DTL_2         PWM4DTLbits.PWM4DTL_2       	/* bit 2 */
#define PWM4DTL_3         PWM4DTLbits.PWM4DTL_3       	/* bit 3 */
#define PWM4DTL_4         PWM4DTLbits.PWM4DTL_4   		/* bit 4 */
#define PWM4DTL_5         PWM4DTLbits.PWM4DTL_5     	/* bit 5 */
#define PWM4DTL_6         PWM4DTLbits.PWM4DTL_6       	/* bit 6 */
#define PWM4DTL_7         PWM4DTLbits.PWM4DTL_7       	/* bit 7 */

// ----- PWMIS Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char PWMIS_0:1;
		unsigned char PWMIS_1:1;
		unsigned char PWMIS_2:1;
		unsigned char PWMIS_3:1;	
		unsigned char PWMIS_4:1;
		unsigned char PWMIS_5:1;
		unsigned char PWMIS_6:1;
		unsigned char PWMIS_7:1;		
	};
} __PWMISbits_t;
extern volatile __PWMISbits_t __at(PWMIS_ADDR) PWMISbits;

#define PWM1S         	PWMISbits.PWMIS_0   		/* bit 0 */
#define IPWM1S         	PWMISbits.PWMIS_1     		/* bit 1 */
#define PWM2S         	PWMISbits.PWMIS_2       	/* bit 2 */
#define IPWM2S         	PWMISbits.PWMIS_3       	/* bit 3 */
#define PWM3S         	PWMISbits.PWMIS_4   		/* bit 4 */
#define IPWM3S         	PWMISbits.PWMIS_5     		/* bit 5 */
#define PWM4S         	PWMISbits.PWMIS_6       	/* bit 6 */
#define IPWM4S         	PWMISbits.PWMIS_7       	/* bit 7 */

// ----- DEADCON Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char DEADCON_0:1;
		unsigned char DEADCON_1:1;
		unsigned char DEADCON_2:1;
		unsigned char DEADCON_3:1;	
		unsigned char DEADCON_4:1;
		unsigned char DEADCON_5:1;
		unsigned char DEADCON_6:1;
		unsigned char DEADCON_7:1;		
	};
} __DEADCONbits_t;
extern volatile __DEADCONbits_t __at(DEADCON_ADDR) DEADCONbits;

#define DEAD1PSR0		DEADCONbits.DEADCON_0   	/* bit 0 */
#define DEAD1PSR1		DEADCONbits.DEADCON_1     	/* bit 1 */
#define DEAD2PSR0		DEADCONbits.DEADCON_2       /* bit 2 */
#define DEAD2PSR1		DEADCONbits.DEADCON_3       /* bit 3 */
#define DEAD1_SEL       DEADCONbits.DEADCON_4   	/* bit 4 */
#define DEAD2_SEL       DEADCONbits.DEADCON_5     	/* bit 5 */
#define DEADT1E         DEADCONbits.DEADCON_6       /* bit 6 */
#define DEADT2E         DEADCONbits.DEADCON_7       /* bit 7 */

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

#define INV1L         	PWMCONbits.PWMCON_0   		/* bit 0 */
#define INV1H         	PWMCONbits.PWMCON_1     	/* bit 1 */
#define INV2L         	PWMCONbits.PWMCON_2       	/* bit 2 */
#define INV2H         	PWMCONbits.PWMCON_3       	/* bit 3 */
#define PWMCON_4      	PWMCONbits.PWMCON_4   		/* bit 4 */
#define PWMCON_5      	PWMCONbits.PWMCON_5     	/* bit 5 */
#define PWMCKS         	PWMCONbits.PWMCON_6       	/* bit 6 */
#define PWMCAS         	PWMCONbits.PWMCON_7       	/* bit 7 */

// ----- DEADT0 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char DEADT0_0:1;
		unsigned char DEADT0_1:1;
		unsigned char DEADT0_2:1;
		unsigned char DEADT0_3:1;	
		unsigned char DEADT0_4:1;
		unsigned char DEADT0_5:1;
		unsigned char DEADT0_6:1;
		unsigned char DEADT0_7:1;		
	};
} __DEADT0bits_t;
extern volatile __DEADT0bits_t __at(DEADT0_ADDR) DEADT0bits;

#define DEADT0_0         DEADT0bits.DEADT0_0   		/* bit 0 */
#define DEADT0_1         DEADT0bits.DEADT0_1     	/* bit 1 */
#define DEADT0_2         DEADT0bits.DEADT0_2       	/* bit 2 */
#define DEADT0_3         DEADT0bits.DEADT0_3       	/* bit 3 */
#define DEADT0_4         DEADT0bits.DEADT0_4   		/* bit 4 */
#define DEADT0_5         DEADT0bits.DEADT0_5     	/* bit 5 */
#define DEADT0_6         DEADT0bits.DEADT0_6       	/* bit 6 */
#define DEADT0_7         DEADT0bits.DEADT0_7       	/* bit 7 */

// ----- DEADT1 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char DEADT1_0:1;
		unsigned char DEADT1_1:1;
		unsigned char DEADT1_2:1;
		unsigned char DEADT1_3:1;	
		unsigned char DEADT1_4:1;
		unsigned char DEADT1_5:1;
		unsigned char DEADT1_6:1;
		unsigned char DEADT1_7:1;		
	};
} __DEADT1bits_t;
extern volatile __DEADT1bits_t __at(DEADT1_ADDR) DEADT1bits;

#define DEADT1_0         DEADT1bits.DEADT1_0   		/* bit 0 */
#define DEADT1_1         DEADT1bits.DEADT1_1     	/* bit 1 */
#define DEADT1_2         DEADT1bits.DEADT1_2       	/* bit 2 */
#define DEADT1_3         DEADT1bits.DEADT1_3       	/* bit 3 */
#define DEADT1_4         DEADT1bits.DEADT1_4   		/* bit 4 */
#define DEADT1_5         DEADT1bits.DEADT1_5     	/* bit 5 */
#define DEADT1_6         DEADT1bits.DEADT1_6       	/* bit 6 */
#define DEADT1_7         DEADT1bits.DEADT1_7       	/* bit 7 */

// ----- INTE0 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char INTE0_0:1;
		unsigned char INTE0_1:1;
		unsigned char INTE0_2:1;
		unsigned char INTE0_3:1;	
		unsigned char INTE0_4:1;
		unsigned char INTE0_5:1;
		unsigned char INTE0_6:1;
		unsigned char INTE0_7:1;		
	};
} __INTE0bits_t;
extern volatile __INTE0bits_t __at(INTE0_ADDR) INTE0bits;

#define TC0IE         	INTE0bits.INTE0_0   		/* bit 0 */
#define P5ICIE         	INTE0bits.INTE0_1     		/* bit 1 */
#define P6ICIE         	INTE0bits.INTE0_2       	/* bit 2 */
#define EX0IE         	INTE0bits.INTE0_3       	/* bit 3 */
#define EX1IE         	INTE0bits.INTE0_4   		/* bit 4 */
#define ADIE         	INTE0bits.INTE0_5     		/* bit 5 */
#define INTE0_6         INTE0bits.INTE0_6       	/* bit 6 */
#define INTE0_7         INTE0bits.INTE0_7       	/* bit 7 */

// ----- INTE1 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char INTE1_0:1;
		unsigned char INTE1_1:1;
		unsigned char INTE1_2:1;
		unsigned char INTE1_3:1;	
		unsigned char INTE1_4:1;
		unsigned char INTE1_5:1;
		unsigned char INTE1_6:1;
		unsigned char INTE1_7:1;		
	};
} __INTE1bits_t;
extern volatile __INTE1bits_t __at(INTE1_ADDR) INTE1bits;

#define TC1IE         	INTE1bits.INTE1_0   		/* bit 0 */
#define TC2IE         	INTE1bits.INTE1_1     		/* bit 1 */
#define DT1IE         	INTE1bits.INTE1_2       	/* bit 2 */
#define DT2IE         	INTE1bits.INTE1_3       	/* bit 3 */
#define DT3IE         	INTE1bits.INTE1_4   		/* bit 4 */
#define DT4IE         	INTE1bits.INTE1_5     		/* bit 5 */
#define INTE1_6         INTE1bits.INTE1_6       	/* bit 6 */
#define INTE1_7         INTE1bits.INTE1_7       	/* bit 7 */

// ----- INTF0 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char INTF0_0:1;
		unsigned char INTF0_1:1;
		unsigned char INTF0_2:1;
		unsigned char INTF0_3:1;	
		unsigned char INTF0_4:1;
		unsigned char INTF0_5:1;
		unsigned char INTF0_6:1;
		unsigned char INTF0_7:1;		
	};
} __INTF0bits_t;
extern volatile __INTF0bits_t __at(INTF0_ADDR) INTF0bits;

#define TC0IF         	INTF0bits.INTF0_0   		/* bit 0 */
#define P5ICIF         	INTF0bits.INTF0_1     		/* bit 1 */
#define P6ICIF         	INTF0bits.INTF0_2       	/* bit 2 */
#define EX0IF         	INTF0bits.INTF0_3       	/* bit 3 */
#define EX1IF         	INTF0bits.INTF0_4   		/* bit 4 */
#define ADIF         	INTF0bits.INTF0_5     		/* bit 5 */
#define INTF0_6         INTF0bits.INTF0_6       	/* bit 6 */
#define INTF0_7         INTF0bits.INTF0_7       	/* bit 7 */

// ----- INTF1 Bits --------------------------------------------------------
typedef union {
	struct {
		unsigned char INTF1_0:1;
		unsigned char INTF1_1:1;
		unsigned char INTF1_2:1;
		unsigned char INTF1_3:1;	
		unsigned char INTF1_4:1;
		unsigned char INTF1_5:1;
		unsigned char INTF1_6:1;
		unsigned char INTF1_7:1;		
	};
} __INTF1bits_t;
extern volatile __INTF1bits_t __at(INTF1_ADDR) INTF1bits;

#define TC1IF         	INTF1bits.INTF1_0   		/* bit 0 */
#define TC2IF         	INTF1bits.INTF1_1     		/* bit 1 */
#define DT1IF         	INTF1bits.INTF1_2       	/* bit 2 */
#define DT2IF         	INTF1bits.INTF1_3       	/* bit 3 */
#define DT3IF         	INTF1bits.INTF1_4   		/* bit 4 */
#define DT4IF         	INTF1bits.INTF1_5     		/* bit 5 */
#define INTF1_6         INTF1bits.INTF1_6       	/* bit 6 */
#define INTF1_7         INTF1bits.INTF1_7       	/* bit 7 */

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

#define IAR_0         	IARbits.IAR_0   		/* bit 0 */
#define IAR_1         	IARbits.IAR_1     		/* bit 1 */
#define IAR_2         	IARbits.IAR_2       	/* bit 2 */
#define IAR_3         	IARbits.IAR_3       	/* bit 3 */
#define IAR_4         	IARbits.IAR_4   		/* bit 4 */
#define IAR_5         	IARbits.IAR_5     		/* bit 5 */
#define IAR_6         	IARbits.IAR_6       	/* bit 6 */
#define IAR_7         	IARbits.IAR_7       	/* bit 7 */

#endif