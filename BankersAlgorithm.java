import java.util.*;

public class BankersAlgorithm {
    // Number of processes and resources
    static int P = 5; // Number of processes
    static int R = 3; // Number of resources

    // Available resources
    static int[] available = new int[R];

    // Maximum resources required by each process
    static int[][] max = new int[P][R];

    // Resources currently allocated to each process
    static int[][] allocation = new int[P][R];

    // Remaining resources needed by each process
    static int[][] need = new int[P][R];

    // Function to calculate if the system is in a safe state
    static boolean isSafe() {
        // Work array is used to simulate the allocation
        int[] work = new int[R];
        boolean[] finish = new boolean[P];

        // Initialize work[] as the available[] array
        for (int i = 0; i < R; i++) {
            work[i] = available[i];
        }

        // Keep track of the number of processes that can finish
        int count = 0;

        while (count < P) {
            boolean found = false;

            // Try to find a process that can finish
            for (int i = 0; i < P; i++) {
                if (!finish[i]) {
                    // Check if the process can be finished
                    boolean canFinish = true;
                    for (int j = 0; j < R; j++) {
                        if (need[i][j] > work[j]) {
                            canFinish = false;
                            break;
                        }
                    }

                    // If it can finish, add its resources to work[]
                    if (canFinish) {
                        for (int j = 0; j < R; j++) {
                            work[j] += allocation[i][j];
                        }
                        finish[i] = true;
                        count++;
                        found = true;
                        break;
                    }
                }
            }

            // If no process can be found that can finish, then the system is in an unsafe state
            if (!found) {
                return false;
            }
        }

        // If all processes can finish, then the system is in a safe state
        return true;
    }

    // Function to request resources
    static boolean requestResources(int process, int[] request) {
        // Check if request is less than or equal to the need of the process
        for (int i = 0; i < R; i++) {
            if (request[i] > need[process][i]) {
                System.out.println("Error: Process has exceeded its maximum claim.");
                return false;
            }
        }

        // Check if request is less than or equal to the available resources
        for (int i = 0; i < R; i++) {
            if (request[i] > available[i]) {
                System.out.println("Error: Not enough resources available.");
                return false;
            }
        }

        // Pretend to allocate the requested resources
        for (int i = 0; i < R; i++) {
            available[i] -= request[i];
            allocation[process][i] += request[i];
            need[process][i] -= request[i];
        }

        // Check if the system is still in a safe state after allocation
        if (isSafe()) {
            System.out.println("Request granted.");
            return true;
        } else {
            // Rollback the changes if the state is unsafe
            for (int i = 0; i < R; i++) {
                available[i] += request[i];
                allocation[process][i] -= request[i];
                need[process][i] += request[i];
            }
            System.out.println("Request denied: System is not in a safe state.");
            return false;
        }
    }

    // Function to initialize the data
    static void initializeData() {
        // Available resources
        available[0] = 3;
        available[1] = 3;
        available[2] = 2;

        // Maximum resource need for each process
        max[0] = new int[] {7, 5, 3};
        max[1] = new int[] {3, 2, 2};
        max[2] = new int[] {9, 0, 2};
        max[3] = new int[] {2, 2, 2};
        max[4] = new int[] {4, 3, 3};

        // Allocation of resources to each process
        allocation[0] = new int[] {0, 1, 0};
        allocation[1] = new int[] {2, 0, 0};
        allocation[2] = new int[] {3, 0, 2};
        allocation[3] = new int[] {2, 1, 1};
        allocation[4] = new int[] {0, 0, 2};

        // Calculate the need matrix (Need = Max - Allocation)
        for (int i = 0; i < P; i++) {
            for (int j = 0; j < R; j++) {
                need[i][j] = max[i][j] - allocation[i][j];
            }
        }
    }

    // Main function
    public static void main(String[] args) {
        // Initialize data for available, max, allocation, and need
        initializeData();

        // Example request
        int process = 1; // Process 1 is requesting resources
        int[] request = {1, 0, 2}; // Process 1 requests 1 unit of resource 0, 0 units of resource 1, and 2 units of resource 2

        // Request resources and check if the system is safe
        requestResources(process, request);
    }
}
