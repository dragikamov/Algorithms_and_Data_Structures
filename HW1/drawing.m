A = load('random.txt');
x_axis = A([1:2:100]);
y_axis = A([2:2:100]);
plot(x_axis, y_axis, 'y');
title('Selection Sort');
xlabel('n');
ylabel('Seconds');
grid on;
hold on;

A = load('best.txt');
x_axis = A([1:2:100]);
y_axis = A([2:2:100]);
plot(x_axis, y_axis, 'b');
hold on;

A = load('worst.txt');
x_axis = A([1:2:100]);
y_axis = A([2:2:100]);
plot(x_axis, y_axis, 'r');
hold on;