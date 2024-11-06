package com.scheduler;
public class FCFS {
    int[] pid;
    int[] ar;
    int[] bt;
    int[] ct;
    int[] ta;
    int[] wt;
    float avgwt;
    float avgta;
    int n;
    public FCFS(int[] pid , int[] ar,int[] bt ) {
        if(pid.length != ar.length || pid.length != bt.length)
            throw new IllegalArgumentException("array length must be same");
        this.n = pid.length;
        this.ar = ar;
        this.bt = bt;
        this.pid = pid;
        this.ct = new int[ar.length];
        this.ta = new int[ar.length];
        this.wt = new int[ar.length];
		this.avgwt=0;
        this.avgta=0;
    }
    
	public void print(){
		System.out.println("\npid  arrival  brust  complete turn waiting");
        for(int  i = 0 ; i< this.n;  i++)
		{
			System.out.println(pid[i] + "  \t " + ar[i] + "\t" + bt[i] + "\t" + ct[i] + "\t" + ta[i] + "\t"  + wt[i] ) ;
		}
        System.out.println("\naverage waiting time: "+ (avgwt/n));     // printing average waiting time.
		System.out.println("average turnaround time:"+(avgta/n));    // printing average turnaround time.
	}
    public void calculate(){
		int temp;
        //sorting according to arrival times
		for(int i = 0 ; i <n; i++)
		{
			for(int  j=0;  j < n-(i+1) ; j++)
			{
				if( ar[j] > ar[j+1] )
				{
					temp = ar[j];
					ar[j] = ar[j+1];
					ar[j+1] = temp;
					temp = bt[j];
					bt[j] = bt[j+1];
					bt[j+1] = temp;
					temp = pid[j];
					pid[j] = pid[j+1];
					pid[j+1] = temp;
				}
			}
		}
		
		// finding completion times
		for(int  i = 0 ; i < n; i++)
		{
			if( i == 0)
			{	
				ct[i] = ar[i] + bt[i];
			}
			else
			{
				if( ar[i] > ct[i-1])
				{
					ct[i] = ar[i] + bt[i];
				}
				else
					ct[i] = ct[i-1] + bt[i];
			}
			ta[i] = ct[i] - ar[i] ;          // turnaround time= completion time- arrival time
			wt[i] = ta[i] - bt[i] ;          // waiting time= turnaround time- burst time
			avgwt += wt[i] ;               // total waiting time
			avgta += ta[i] ;               // total turnaround time
		}
    }
}