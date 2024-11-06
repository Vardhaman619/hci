import java.util.Arrays;
import java.util.Comparator;

public class MemoryAllocation {

    // Best Fit
    public static void bestFit(int[] memoryBlocks, int[] processes) {
        int[] allocation = new int[processes.length];

        // Initially, no memory block is allocated
        Arrays.fill(allocation, -1);

        // Iterate through all processes and allocate memory
        for (int i = 0; i < processes.length; i++) {
            int bestIdx = -1;
            for (int j = 0; j < memoryBlocks.length; j++) {
                if (memoryBlocks[j] >= processes[i]) {
                    if (bestIdx == -1 || memoryBlocks[j] < memoryBlocks[bestIdx]) {
                        bestIdx = j;
                    }
                }
            }

            if (bestIdx != -1) {
                allocation[i] = bestIdx;
                memoryBlocks[bestIdx] -= processes[i]; // Allocate the memory
            }
        }

        System.out.println("\nBest Fit Allocation:");
        printAllocation(allocation, processes, memoryBlocks);
    }

    // Worst Fit
    public static void worstFit(int[] memoryBlocks, int[] processes) {
        int[] allocation = new int[processes.length];

        // Initially, no memory block is allocated
        Arrays.fill(allocation, -1);

        // Iterate through all processes and allocate memory
        for (int i = 0; i < processes.length; i++) {
            int worstIdx = -1;
            for (int j = 0; j < memoryBlocks.length; j++) {
                if (memoryBlocks[j] >= processes[i]) {
                    if (worstIdx == -1 || memoryBlocks[j] > memoryBlocks[worstIdx]) {
                        worstIdx = j;
                    }
                }
            }

            if (worstIdx != -1) {
                allocation[i] = worstIdx;
                memoryBlocks[worstIdx] -= processes[i]; // Allocate the memory
            }
        }

        System.out.println("\nWorst Fit Allocation:");
        printAllocation(allocation, processes, memoryBlocks);
    }

    // Optimal Fit (simple version)
    public static void optimalFit(int[] memoryBlocks, int[] processes) {
        int[] allocation = new int[processes.length];

        // Initially, no memory block is allocated
        Arrays.fill(allocation, -1);

        // Iterate through all processes and allocate memory
        for (int i = 0; i < processes.length; i++) {
            int optimalIdx = -1;
            int minWaste = Integer.MAX_VALUE;

            for (int j = 0; j < memoryBlocks.length; j++) {
                if (memoryBlocks[j] >= processes[i]) {
                    int waste = memoryBlocks[j] - processes[i];
                    if (waste < minWaste) {
                        minWaste = waste;
                        optimalIdx = j;
                    }
                }
            }

            if (optimalIdx != -1) {
                allocation[i] = optimalIdx;
                memoryBlocks[optimalIdx] -= processes[i]; // Allocate the memory
            }
        }

        System.out.println("\nOptimal Fit Allocation:");
        printAllocation(allocation, processes, memoryBlocks);
    }

    // Helper function to print memory allocation
    public static void printAllocation(int[] allocation, int[] processes, int[] memoryBlocks) {
        System.out.println("Process No.\tProcess Size\tBlock No.\tBlock Size");
        for (int i = 0; i < processes.length; i++) {
            if (allocation[i] != -1) {
                System.out.println((i + 1) + "\t\t" + processes[i] + "\t\t" + (allocation[i] + 1) + "\t\t" + memoryBlocks[allocation[i]]);
            } else {
                System.out.println((i + 1) + "\t\t" + processes[i] + "\t\t" + "Not Allocated");
            }
        }
    }

    public static void main(String[] args) {
        int[] memoryBlocks = {100, 500, 200, 300, 600}; // Memory block sizes
        int[] processes = {212, 417, 112, 426};         // Process sizes

        // Best Fit Allocation
        bestFit(Arrays.copyOf(memoryBlocks, memoryBlocks.length), Arrays.copyOf(processes, processes.length));

        // Worst Fit Allocation
        worstFit(Arrays.copyOf(memoryBlocks, memoryBlocks.length), Arrays.copyOf(processes, processes.length));

        // Optimal Fit Allocation
        optimalFit(Arrays.copyOf(memoryBlocks, memoryBlocks.length), Arrays.copyOf(processes, processes.length));
    }
}
