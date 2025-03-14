function [VV,pC]= EulerPC()
    dt=1; %time interval =1ms
    x=0:dt:1000;
    V=[];
    w=[];
    VV=[];
    Vr=-58;
    b=260;
    el=-65;
    pC=[];
    i=1;
    flg=0;
    V(i)=-60;
    w(i)=V-el;
    PCspik=0;
    I=0;
    for t=x

        V(i+1)=V(i)+dt*(VoltagePC(V(i),w(i),I));
        w(i+1)=w(i)+dt*(AdCurrentPC(V(i),w(i)));
        %gc=gc+dt*(synaptic_conductance(gc));
        
        if V(i+1) > 30
            VV(end+1)=30;
            V(i+1)=Vr;

            w(i+1)=w(i+1)+b;
            flg=0;
        else
            VV(end+1)=V(i+1);
        end
        
        if (V(i+1)>-40)&&(flg==0)
            flg=1;
            PCspik=PCspik+1;
            pC(end+1)=t; % store spike time
        end
        i=i+1;
    end
    PCspik
    plot(x,VV)
end