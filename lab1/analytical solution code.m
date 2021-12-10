clear
clc

% variables
m = 68.1;
c = 12.5;
g = 9.8;
vx = 44.87;
tx = 10;

% analytical solution
t=[10:-1:0];
v = m*g/c-(m/c)*(g-c*vx/m)*exp(-c*(t-tx)/m);
plot(t,v,'-k');
grid on;
legend('Analytical Solution');
xlabel('Time(s)');
ylabel('Velocity(m/s)');