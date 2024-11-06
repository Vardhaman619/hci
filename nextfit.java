import java.util.Scanner;

public class NextFit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

     
        System.out.print("Enter the number of memory blocks: ");
        int numBlocks = scanner.nextInt();
        int[] memoryBlocks = new int[numBlocks];
        boolean[] isBlockUsed = new boolean[numBlocks]; 

      
        System.out.println("Enter the size of each memory block:");
        for (int i = 0; i < numBlocks; i++) {
            memoryBlocks[i] = scanner.nextInt();
        }

        
        System.out.print("Enter the number of processes: ");
        int numProcesses = scanner.nextInt();
        int[] processSizes = new int[numProcesses];

       
        System.out.println("Enter the size of each process:");
        for (int i = 0; i < numProcesses; i++) {
            processSizes[i] = scanner.nextInt();
        }

        int lastAllocatedIndex = 0; 
        for (int i = 0; i < numProcesses; i++) {
            boolean allocated = false;
            for (int j = 0; j < numBlocks; j++) {
                int index = (lastAllocatedIndex + j) % numBlocks;
                
                if (!isBlockUsed[index] && memoryBlocks[index] >= processSizes[i]) {
                    System.out.println("Process " + (i + 1) + " of size " + processSizes[i] + " allocated to block " + (index + 1));
                    memoryBlocks[index] -= processSizes[i];
                    isBlockUsed[index] = true; 
                    lastAllocatedIndex = index; 
                    allocated = true;
                    break;
                }
            }
            if (!allocated) {
                System.out.println("Process " + (i + 1) + " of size " + processSizes[i] + " could not be allocated.");
            }
        }

        scanner.close();
    }
}
