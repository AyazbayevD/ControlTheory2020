syms x(t) s
Dx = diff(x, t);
eqn = diff(x, t, 2) == sin(4 * t) - Dx * 2 + x * 3;    
eqnLT = laplace(eqn, t, s);
syms x_LT
eqnLT = subs(eqnLT, laplace(x, t, s), x_LT);
x_LT = solve(eqnLT, x_LT);
xSol = ilaplace(x_LT, s, t);
xSol = simplify(xSol);
vars = [x(0), Dx(0)];
values = [2, 3];
xSol(t) = subs(xSol, vars, values);
disp(xSol(t));