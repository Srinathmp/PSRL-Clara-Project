
    #include <stdio.h>
    int main (){
        int a,c1=0,c2=0,n;
        scanf("%d",&n);
        while(n--){
            scanf("%d",&a);
            if(a%2!=0){
                c1+=1;
            }
            else
                c2+=1;    
            }
        if(c2>c1)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
        return 0;
    }

