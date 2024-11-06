import java.util.*;

class Process {
    int id; // Process ID
    int burstTime; // Burst Time
    int priority; // Priority

    public Process(int id, int burstTime, int priority) {
        this.id = id;
        this.burstTime = burstTime;
        this.priority = priority;
    }
}

class PriorityScheduling {
    // Function to perform priority scheduling
    public static void priorityScheduling(Process[] processes) {
        // Sorting processes based on priority (higher priority first)
        Arrays.sort(processes, new Comparator<Process>() {
            public int compare(Process p1, Process p2) {
                return p2.priority - p1.priority; // Descending order
            }
        });

        int totalTime = 0; // Time elapsed
        int totalWaitingTime = 0; // Total waiting time
        int totalTurnaroundTime = 0; // Total turnaround time

        System.out.println("Process ID\tBurst Time\tPriority\tWaiting Time\tTurnaround Time");

        // Calculate and print waiting and turnaround times for each process
        for (Process p : processes) {
            int waitingTime = totalTime; // Waiting time is the time before the process starts executing
            int turnaroundTime = waitingTime + p.burstTime; // Turnaround time = waiting time + burst time

            totalWaitingTime += waitingTime;
            totalTurnaroundTime += turnaroundTime;

            // Print details of the process
            System.out.println(p.id + "\t\t" + p.burstTime + "\t\t" + p.priority + "\t\t" + waitingTime + "\t\t" + turnaroundTime);

            totalTime += p.burstTime; // Update total time after the process executes
        }

        // Calculate average waiting time and turnaround time
        double averageWaitingTime = (double) totalWaitingTime / processes.length;
        double averageTurnaroundTime = (double) totalTurnaroundTime / processes.length;

        System.out.println("\nAverage Waiting Time: " + averageWaitingTime);
        System.out.println("Average Turnaround Time: " + averageTurnaroundTime);
    }

    public static void main(String[] args) {
        // Create some processes with ID, Burst Time and Priority
        Process[] processes = {
            new Process(1, 6, 2),
            new Process(2, 8, 1),
            new Process(3, 7, 3),
            new Process(4, 3, 4)
        };

        // Call the scheduling function
        priorityScheduling(processes);
    }
}
