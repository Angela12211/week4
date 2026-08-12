# # robot_location = "Room3"
# # print(robot_location)


# # rooms = ["Room1", "Room2", "Room3"]
# # print [rooms]
# # print(len(rooms))


# # robot_status = {
# #     "location" : "Room 3",
# #     "battery" : 80,
# #     "carrying_item" : False
# # }
# # print(robot_status['location'])



# # state= "off" 

# # def toggle(state):
# #     return "on" if state == "off" else "off"

# # state = toggle(state)
# # print(state)



# # connections = { #rules
# #     "Room 1" : ["Room2"],
# #     "Room 2" : ["Room1", "Room2"],
# #     "Room 3" : ["Room5", "Room1", "Room3"],
# #     "Room 4" : ["Room4"],
# # }
# # current_state = "Room 3" #states
# # print("Possible actions", connection[current_state]) #actions


# # def can_dispense(balance, price): #rules
# #     return balance >= price

# # balance, price = 20, 15 #states
# # if can_dispense(balance,price): #rules
# #     balance -= price #action
# #     print("Dispensed. Remaining", balance) 
# # else:
# #     print("Blocked: Insufficient balance")


#ai
# reports = []
# next_report_id = 1

# VALID_INCIDENT_TYPES = ["lost id", "room issue", "lab equipment damage", "bullying"]

# def determine_initial_status(incident_type, description, priority, has_evidence):
#     if incident_type.lower() not in VALID_INCIDENT_TYPES:
#         return "Rejected"

#     if len(description.strip()) < 10:
#         return "needs revision"

#     if priority.lower() == "high" and has_evidence:
#         return "For Review"

#     return "On Progress"

# def submit_report():
#     global next_report_id

#     print("\n=== SUBMIT NEW REPORT ===")
#     name = input("Enter reporter name: ").strip()
#     incident_type = input("Enter incident type (lost id / room issue / lab equipment damage / bullying):\n").strip()
#     priority = input("Enter priority (low / medium / high):\n").strip()
#     description = input("Enter incident description:\n").strip()
#     evidence_input = input("Is there evidence attached? (yes/no):\n").strip().lower()
    
#     has_evidence = evidence_input == "yes"

#     status = determine_initial_status(incident_type, description, priority, has_evidence)

#     report = {
#         "id": next_report_id,
#         "name": name,
#         "incident_type": incident_type,
#         "priority": priority,
#         "description": description,
#         "has_evidence": has_evidence,
#         "status": status
#     }

#     reports.append(report)
#     print("\nReport submitted successfully.")
#     print(f"Assigned Report ID: {next_report_id}")
#     print(f"Current Status: {status}")

#     next_report_id += 1

# def review_reports():
#     print("\n=== ALL SUBMITTED REPORTS ===")
#     if not reports:
#         print("No reports submitted yet.")
#         return

#     for r in reports:
#         print(f"\nReport ID: {r['id']}")
#         print(f"Reporter Name: {r['name']}")
#         print(f"Incident Type: {r['incident_type']}")
#         print(f"Priority: {r['priority']}")
#         print(f"Description: {r['description']}")
#         print(f"Evidence Attached: {r['has_evidence']}")
#         print(f"Current Status: {r['status']}")

# def update_report_status():
#     if not reports:
#         print("\nNo reports available to update.")
#         return

#     print("\n=== UPDATE REPORT STATUS ===")
#     for r in reports:
#         print(f"\nReport ID: {r['id']}")
#         print(f"Reporter Name: {r['name']}")
#         print(f"Incident Type: {r['incident_type']}")
#         print(f"Priority: {r['priority']}")
#         print(f"Description: {r['description']}")
#         print(f"Evidence Attached: {r['has_evidence']}")
#         print(f"Current Status: {r['status']}")

#     try:
#         target_id = int(input("\nEnter Report ID to update: "))
#     except ValueError:
#         print("Invalid ID format.")
#         return

#     selected_report = None
#     for r in reports:
#         if r['id'] == target_id:
#             selected_report = r
#             break

#     if not selected_report:
#         print("Report ID not found.")
#         return

#     print(f"Current Status: {selected_report['status']}")
#     print("\nAllowed New Status: On Progress, For Review, Completed, Rejected, Needs Revision")
    
#     new_status = input("\nEnter new status: ").strip()

#     allowed_statuses = ["On Progress", "For Review", "Completed", "Rejected", "Needs Revision"]
    
#     matched_status = None
#     for status_option in allowed_statuses:
#         if status_option.lower() == new_status.lower():
#             matched_status = status_option
#             break

#     if matched_status:
#         selected_report['status'] = matched_status
#         print("Status updated successfully.")
#         print(f"New Status: {matched_status}")
#     else:
#         print("Invalid status option.")

# def count_reports_by_status():
#     print("\n=== REPORT STATUS COUNTS ===")
    
#     counts = {
#         "For Review": 0,
#         "Completed": 0,
#         "On Progress": 0,
#         "Rejected": 0,
#         "Needs Revision": 0
#     }

#     for r in reports:
#         status = r['status']
#         for key in counts:
#             if key.lower() == status.lower():
#                 counts[key] += 1

#     print(f"For Review: {counts['For Review']}")
#     print(f"Completed: {counts['Completed']}")
#     print(f"On Progress: {counts['On Progress']}")

# def main():
#     while True:
#         print("\n=== STUDENT INCIDENT REPORT MANAGEMENT SYSTEM ===")
#         print("1. Submit a new report")
#         print("2. Review all submitted reports")
#         print("3. Update report status")
#         print("4. Count reports by status")
#         print("5. Exit")

#         choice = input("Enter your choice: ").strip()

#         if choice == "1":
#             submit_report()
#         elif choice == "2":
#             review_reports()
#         elif choice == "3":
#             update_report_status()
#         elif choice == "4":
#             count_reports_by_status()
#         elif choice == "5":
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please enter 1-5.")

# if __name__ == "__main__":
#     main()





# # maze= {"A" : ["B"], "B" : ["A", "C"], "C": ["B", "D"], "D" : ["C"]}



# # start, goal = "A", "D"
# # frontier = maze[start]
# # search_space = list(maze.keys())

# # start = "B"
# # start = "C"
# # frontier = goal

# # print(frontier)
# # print(search_space)
# # print(goal in frontier)



# # maze = {
# #     "A" : ["B", "C"],
# #     "B" : ["A", "D", "E"],
# #     "C" : ["A", "F"],
# #     "D" : ["B"],
# #     "E" : ["B"],
# #     "F" : ["C", "G"],
# #     "D" : ["F"],    
# # }

# # def dfs_find_path(maze,start,goal,path=None):
# #     if path is None:
# #         path = [start]

# #     else:
# #         path = path + [start]

# #     print("Visiting:", start, "| Path so far:", path )

# #     if start == goal:
# #         return path
    
# #     for neighbor  in maze[start]:
# #         if neighbor not in path:
# #             result = dfs_find_path(maze,neighbor,goal,path)
# #             if result:
# #                 return result

# #     return None
# # print(dfs_find_path)



# # maze = {
# #     "A": ["B", "C"],
# #     "B": ["A", "D", "E"],
# #     "C": ["A", "F"],
# #     "D": ["B", "F"],  
# #     "E": ["B"],
# #     "F": ["C", "G"],
# #     "G": ["F"],        
# # }

# # def dfs_find_path(maze, start, goal, path=None):
# #     if path is None:
# #         path = [start]
# #     else:
# #         path = path + [start]

# #     print("Visiting:", start, "| Path so far:", path)

# #     if start == goal:
# #         return path
    
   
# #     for neighbor in maze.get(start, []):
# #         if neighbor not in path:
# #             result = dfs_find_path(maze, neighbor, goal, path)
# #             if result:
# #                 return result

# #     return None

# # # Execute the search from 'A' to 'G'
# # final_path = dfs_find_path(maze, "A", "G")
# # print("\nFinal Path Found:", final_path)


# from collection import deque

# maze = {
#     "A" : ["C", "D"],
#     "B" : ["A", "C", "B"],
#     "C" : ["D", "E"],
#     "D" : ["A", "B"],
#     "E" : ["A", "G"],
#     "F" : ["D", "F"],
#     "G" : ["A"],
# }

# def bfs_find_path(maze,start,goal):
#     queue = deque ([start])
#     visited = set()


#     while queue:
#         path = queue.popleft()
#         node = path[-1]


#         print("Exploring:", path)

#         if node == goal: 
#             return path 

#         if node not in visited:
#             visited.add(node)
#             for neighbor in  maze[node]:
#                 queue.append(path + [neighbor])
#     return None
# print (bfs_find_path(maze, "A","G"))