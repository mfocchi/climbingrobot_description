from cartesian_interface.pyci_all import *

cli = pyci.CartesianInterfaceRos()

print(cli)

task_name = 'base_link'
base_link = cli.getTask(task_name)

initial_pose, _, _ = base_link.getPoseReference() # [0] for pose, [1] for velocity
print('Task current pose reference is \n{}'.format(initial_pose))
print('Task current vel reference is \n{}'.format(base_link.getPoseReference()[1])) # [0] for pose, [1] for velocity

# GO TO START POSE
pose_ref = initial_pose
pose_ref.translation[0] = 0.3
time = 3.
base_link.setPoseTarget(pose_ref, time)
base_link.waitReachCompleted(5.0) # blocks till action is completed (or timeout has passed)

print("Press a button to continue...")
ans = input().split(' ')[0]

# GO TO GOAL POSE
pose_ref.translation[0] = 0.3
pose_ref.translation[1] = 4.
pose_ref.translation[2] = 12.
time = 10.
base_link.setPoseTarget(pose_ref, time)
base_link.waitReachCompleted(15.0) # blocks till action is completed (or timeout has passed)

