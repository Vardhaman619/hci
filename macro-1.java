import java.io.*;
public class MPass1 {

	public static void main(String[] args)throws IOException {
		BufferedReader br1 = new BufferedReader(new FileReader("D:\\TCOB22\\MacroAssembler\\src\\input3.txt"));
        String line;
		mdt[] MDT = new mdt[20];
		mnt[] MNT = new mnt[4];
		arglist[] ARGLIST = new arglist[10];
		boolean macro_start = false,fill_arglist = false,macro_end = false;
		int mdt_cnt = 0,mnt_cnt = 0,arglist_cnt = 0;
		while((line = br1.readLine())!=null)
		{
			line = line.replaceAll(","," ");
			String[] tokens = line.split("\\s+");
			MDT[mdt_cnt] = new mdt();
			String stmnt = "";
			for(int i = 0;i<tokens.length;i++)
			{
				if(tokens[i].equalsIgnoreCase("mend"))
				{
					MDT[mdt_cnt++].stmnt = "\t" + tokens[i];
					macro_end = true;
				}
				if(tokens[i].equalsIgnoreCase("macro"))
				{
					macro_start = true;
					macro_end = false;
				}
				else if(!macro_end)
				{
					if(macro_start)
					{
						MNT[mnt_cnt++] = new mnt(tokens[i],mdt_cnt);
						macro_start = false;
						fill_arglist = true;
					}
					if(fill_arglist)
					{
						while(i<tokens.length)
						{
							MDT[mdt_cnt].stmnt = MDT[mdt_cnt].stmnt + "\t" + tokens[i];
							stmnt = stmnt + "\t" + tokens[i];
							if(tokens[i].matches("&[a-zA-Z]+") || tokens[i].matches("&[a-zA-Z]+[0-9]+")) 
							{
								ARGLIST[arglist_cnt++] = new arglist(tokens[i]);
							}
							i++;
						}
						fill_arglist = false;
					}
					else
					{
						if(tokens[i].matches("[a-zA-Z]+") || tokens[i].matches("[a-zA-Z]+[0-9]") || tokens[i].matches("[0-9]+"))
						{
							MDT[mdt_cnt].stmnt = MDT[mdt_cnt].stmnt + "\t" + tokens[i];
							stmnt = stmnt + "\t" + tokens[i];
						}
						if(tokens[i].matches("&[a-zA-Z]+") || tokens[i].matches("&[a-zA-Z]+[0-9]" ))
						{
							for(int j =0;j<arglist_cnt;j++)
							{
								if(tokens[i].equals(ARGLIST[j].argname))
								{
									MDT[mdt_cnt].stmnt = MDT[mdt_cnt].stmnt + "\t #" + (j+1);
									stmnt = stmnt +"\t #" + (j+1);
								}
							}
						}
					}
				}
			}
			if(stmnt!="" && !macro_end)
				mdt_cnt++;
		}
		br1.close();
			
		BufferedWriter bw1=new BufferedWriter(new      FileWriter("D:\\TCOB22\\MacroAssembler\\src\\MNT.txt"));
		System.out.println("\n\t*MACRO NAME TABLE*");
		System.out.print("\n\tINDEX\tNAME\tADDRESS \n");
		
		for(int i=0;i<mnt_cnt;i++)
		{
			System.out.println("\t" + i + "\t" + MNT[i].name + "\t" + MNT[i].addr);
			
		}
		
		bw1=new BufferedWriter(new FileWriter("D:\\TCOB10\\MacroAssembler\\src\\MDT.txt"));
		System.out.println("\n\t*ARGUMENT LIST*");
		System.out.print("\n\tINDEX\tNAME\tADDRESS \n");
		
		for(int i=0;i<arglist_cnt;i++)
		{
			System.out.println("\t" + i + "\t" + ARGLIST[i].argname );
		}
		System.out.println("\n\t*MACRO DEFINITION TABLE*");
		System.out.print("\n\tINDEX\tSTATEMENT \n");
		bw1=new BufferedWriter(new FileWriter("D:\\TCOB22\\MacroAssembler\\src\\MDT.txt"));
		for(int i=0;i<mdt_cnt;i++)
		{
			System.out.println("\t" + i + "\t" + MDT[i].stmnt);
			
		}
	}
public class mnt {
	String name;
	int addr;
	int arg_cnt;
	mnt(String nm,int address)
	{
		this.name=nm;
		this.addr=address;
		this.arg_cnt=0;
	}
}

public class mdt
{
	String stmnt;
	public mdt()
	{
		stmnt="";
	}
}
public class arglist
{
	String argname;
	arglist(String argument)
	{
		this.argname=argument;
	}
}
MACRO
INCR &X,&Y,&REG1=AREG
MOVER &REG1,&X
ADD &REG1,&Y
MOVEM &REG1,&X
MEND
MACRO
DECR &A,&B,&REG2=BREG
MOVER &REG2,&A
SUB &REG2,&B
MOVEM &REG2,&A
MEND
START 100
READ N1
READ N2
DECR N1,N2
INCR N1,N2
STOP
N1 DS 1
N2 DS 2
END
