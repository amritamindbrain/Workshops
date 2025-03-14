%Reconstructing the firing behavior of cerebellar granule cell  

function [VV,PC_times,temp,n]=EulerGrC()
    dt=1; % time interval 1ms
    time=1000;% time duration
    x=0:dt:time; % x contains the time interval

    V=[];    w=[];    VV=[];    PC_times=[];    temp=[];
    j=1;    n=0;        flg=0;    i=1;

    Vr=-64;
    b=250;
    el=-70;

    V(i)=-70;
    w(i)=V-el;
    cnt=1;
    I=450;
    figure()

    for t=x
        %euler method for ODE
        V(i+1)=V(i)+dt*(feval('VoltageGrC',V(i),w(i),I));
        w(i+1)=w(i)+dt*(feval('AdCurrentGrC',V(i),w(i)));
                
        if V(i+1) > 30
            VV(end+1)=30;
            V(i+1)=Vr;
            w(i+1)=w(i+1)+b;
            flg=0;
        else
            VV(end+1)=V(i+1);
        end
        i=i+1;
        
        if (V(i)>-40)&&(flg==0)
            flg=1;
            PC_times(1,j)=1; % set activity=1 at the time of spike
            n=n+1;
            temp(1,cnt)=t;
            cnt=cnt+1;

        else
            PC_times(1,j)=0;
        end
        j=j+1;

    end
   
    plot(x,VV)

end