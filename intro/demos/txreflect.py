from numpy import zeros

def txreflect (ZD, ZR, Z0, T, Vd):
    """

    VD, VR = txreflect (ZD, ZR, Z0, T, Vd)
    
    Calculate transmission line reflections, where
    
    ZD -- driver impedance
    ZR -- receiver impedance
    Z0 -- transmission line characteristic impedance
    T  -- transmission line delay (time samples)
    Vd -- drive signal  
    
    VD -- voltage signal calculated at driver
    VR -- voltage signal calculated at receiver
    
    This models the transmission line as a simple delay line
    with characteristic impedance Z0 and propagation delay T.  
    
    M. P. Hayes
    ECE June 2003/2020
    """
    
    # Reflection coefficients.
    Gamma_D = (ZD - Z0) / (ZD + Z0)
    Gamma_R = (ZR - Z0) / (ZR + Z0)
    
    
    print('Gamma_D = %.3f, Gamma_R = %.3f' % (Gamma_D, Gamma_R))

    N = len(Vd)
    
    # Voltage pulse travelling from driver to receiver.
    vt1 = zeros(N)
    
    # Voltage pulse travelling from receiver to driver.
    vt2 = zeros(N)
    
    # Voltage at driver.
    VD = zeros(N)
    
    # Voltage at receiver.
    VR = zeros(N)
    
    for n in range(N):
        
        # Determine voltage pulse coming out of transmission line at driver.
        if (n > T):
            VpD = vt2[n - T]
        else:
            VpD = 0
            
        # Relect wave back into transmission line taking into account
        # attenuation of driving signal Vd by ratio of Z0 to Z0 + ZD.
        vt1[n] = (Vd[n] * Z0) / (ZD + Z0) + Gamma_D * VpD
            
        # Calculate voltage at transmitter.
        VD[n] = vt1[n] + VpD
        
        # Determine voltage pulse coming out of transmission line at receiver.
        if (n > T):
            VpR = vt1[n - T]
        else:
            VpR = 0
    
        # Relect wave back into transmission line.
        vt2[n] = Gamma_R * VpR
        
        # Calculate voltage at receiver.
        VR[n] = vt2[n] + VpR

    return VD, VR

