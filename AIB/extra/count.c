#include <stdio.h>

int ft_atoi(char *str)
{
    int i = 0;
    int res = 0;

    while (str[i] == ' ')
        i++;
    while(str[i] >= '0' && str[i] <= '9')
    {
        res = res * 10 + (str[i] - '0');
        i++;
    }
    return (res);
}


int main(int argc, char **argv)
{
    int i = 0;
    int num = ft_atoi(argv[1]);
    int soma = 0;

    while (num > 9)
    {
        soma = soma + num % 10;
        num = num / 10;
    }
    soma = soma + num;
    printf("%d", soma);

}
