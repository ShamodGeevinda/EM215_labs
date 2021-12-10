clear
clc
m = 68.1;
c = 12.5;
g = 9.8;
vx = 44.87;
tx = 10;

t=[10:-1:0];
v = m*g/c-(m/c)*(g-c*vx/m)*exp(-c*(t-tx)/m);
%plot(t,v,'k');


v1 = 44.87;
t1 = 10;
delt =1;
res_delt = delt;
TV = [t1,v1];
while 1
    t2 = t1 - delt;
    v2 = (g-c/m*v1)*(t2-t1)+v1;
    %t2 = 10 - delt;
    delt = delt+res_delt;
    if t2<0
        break
    end
    TV = [TV;[t2,v2]];
    v1 = v2;
    t1 = t2;
end

plot(t,v,'.k'); hold on;
plot(TV(:,1),TV(:,2),'.-r');
grid on;
legend('Analytical Solution','Numerical Solution')
xlabel('Time(s)');
ylabel('Velocity(m/s)');