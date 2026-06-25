# include <stdio.h>

int main() {
    // & = address of operator

    // C calculator 
    double num1, num2, result;
    char operator;

    // Numbers input and operator
    printf("Enter first number: ");
    scanf("%lf", &num1);
    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &operator);
    printf("Enter second number: ");
    scanf("%lf", &num2);

    // Calculation
    if (operator == '+') {
        result = num1 + num2;
        printf("%lf\n", result);
    } else if (operator == '-') {
        result = num1 - num2;
        printf("%lf\n", result);
    } else if (operator == '*') {
        result = num1 * num2;
        printf("%lf\n", result);
    } else if (operator == '/') {
        result = num1 / num2;
        printf("%lf\n", result);
    } else {
        printf("Invalid operator\n");
    }

    return 0;
}