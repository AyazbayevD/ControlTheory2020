syms x(t)
Dx = diff(x, t);
eqn = diff(x, t, 2) == sin(4 * t) - Dx * 2 + x * 3;    
cond = [x(0) == 2, Dx(0) == 3];
xSol(t) = dsolve(eqn, cond);
xSol(t) = simplify(xSol(t));
disp(xSol(t));
var = 0:0.001:10;
plot(var, xSol(var));
