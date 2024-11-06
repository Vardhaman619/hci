import java.util.*;

class Process {
    int id; // Process ID
    int burstTime; // Total burst time for the process
    int remainingTime; // Remaining burst time for the process (used in preemptive scheduling)
    int priority; // Priority of the process
    int arrivalTime; // Arrival time of the process

    public Process(int id, int burstTime, int priority, int arrivalTime) {
        this.id = id;
        this.burstTime = burstTime;
        this.remainingTime = burstTime; // Initially, remaining time is same as burst time
        this.priority = priority;
        this.arrivalTime = arrivalTime;
    }
}

class PreemptivePriorityScheduling {
    public static void preemptivePriorityScheduling(Process[] processes) {
        int n = processes.length;
        int totalTime = 0; // The current time (also used as the CPU time)
        int completed = 0; // To keep track of completed processes
        int totalWaitingTime = 0;
        int totalTurnaroundTime = 0;

        // Priority queue to select the process with the highest priority (lower priority value means higher priority)
        PriorityQueue<Process> pq = new PriorityQueue<>(Comparator.comparingInt(p -> p.priority));

        // Keep track of the processes that are still in the queue
        int[] waitingTime = new int[n];
        int[] turnaroundTime = new int[n];

        // Keep track of whether the process is completed
        boolean[] isCompleted = new boolean[n];
        
        // Run until all processes are completed
        while (completed < n) {
            // Add all processes that have arrived by current time to the priority queue
            for (Process p : processes) {
                if (!isCompleted[p.id - 1] && p.arrivalTime <= totalTime) {
                    pq.add(p);
                }
            }

            // If there's a process ready to be executed
            if (!pq.isEmpty()) {
                Process current = pq.poll(); // Get the process with the highest priority

                // If the remaining time of the current process is greater than 1
                // we will execute it for 1 unit of time and then push it back to the queue
                if (current.remainingTime > 1) {
                    current.remainingTime--;
                    pq.add(current); // Re-insert the process into the priority queue with updated remaining time
                } else {
                    // If the process has finished, update the waiting time and turnaround time
                    isCompleted[current.id - 1] = true;
                    completed++;

                    // Turnaround time is the total time minus arrival time
                    turnaroundTime[current.id - 1] = totalTime + 1 - current.arrivalTime;
                    waitingTime[current.id - 1] = turnaroundTime[current.id - 1] - current.burstTime;

                    totalWaitingTime += waitingTime[current.id - 1];
                    totalTurnaroundTime += turnaroundTime[current.id - 1];
                }
            }

            totalTime++; // Increment the time after each cycle (each unit of time)
        }

        // Display results
        System.out.println("Process ID\tBurst Time\tArrival Time\tPriority\tWaiting Time\tTurnaround Time");
        for (int i = 0; i < n; i++) {
            System.out.println((i + 1) + "\t\t" + processes[i].burstTime + "\t\t" + processes[i].arrivalTime + "\t\t"
                    + processes[i].priority + "\t\t" + waitingTime[i] + "\t\t" + turnaroundTime[i]);
        }

        // Calculate average waiting time and turnaround time
        double avgWaitingTime = (double) totalWaitingTime / n;
        double avgTurnaroundTime = (double) totalTurnaroundTime / n;

        System.out.println("\nAverage Waiting Time: " + avgWaitingTime);
        System.out.println("Average Turnaround Time: " + avgTurnaroundTime);
    }

    public static void main(String[] args) {
        // Example processes with (id, burst time, priority, arrival time)
        Process[] processes = {
            new Process(1, 6, 2, 0),
            new Process(2, 8, 1, 1),
            new Process(3, 7, 3, 2),
            new Process(4, 3, 4, 3)
        };

        // Call the preemptive priority scheduling function
        preemptivePriorityScheduling(processes);
    }
}
