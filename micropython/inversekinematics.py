import numpy as np

# 1. Robot dimensions (meters)
L1 = 0.05  # Coxa length
L2 = 0.10  # Femur length
L3 = 0.12  # Tibia length


# 2. Inverse kinematics: (x, y, z) → (theta1, theta2, theta3)
def inverse_kinematics(x, y, z):
    # Coxa rotation
    print(x, y, z)
    theta1 = np.arctan2(y, x)

    # Projected distance in horizontal plane minus coxa
    xy_dist = np.hypot(x, y)
    x_proj = xy_dist - L1

    # Distance from femur base to foot
    r = np.hypot(x_proj, z)

    # Law of cosines for tibia (theta3)
    cos_theta3 = (L2**2 + L3**2 - r**2) / (2 * L2 * L3)
    cos_theta3 = np.clip(cos_theta3, -1.0, 1.0)
    theta3 = np.arccos(cos_theta3)

    # Femur angle components
    phi = np.arctan2(z, x_proj)
    alpha = np.arctan2(L3 * np.sin(theta3), L2 + L3 * np.cos(theta3))
    theta2 = phi - alpha

    return theta1, theta2, theta3


# 3. Generate a forward‐step trajectory
def foot_trajectory(stride=0.06, height=0.02, steps=50):
    """
    Creates a cycloidal swing & linear stance trajectory.
    stride: total forward distance
    height: max lift of foot
    steps: total samples per cycle
    """
    for i in range(steps):
        t = i / (steps - 1)
        # Swing: first half of cycle
        if t <= 0.5:
            s = t / 0.5
            x = -stride / 2 + stride * s
            z = height * np.sin(np.pi * s)
        # Stance: return on ground
        else:
            s = (t - 0.5) / 0.5
            x = stride / 2 - stride * s
            z = 0.0

        # Y remains constant (leg plane)
        y = 0.0
        yield x, y, z


# 4. Main loop: compute and print joint angles
if __name__ == "__main__":
    print("Step\ttheta1 (°)\ttheta2 (°)\ttheta3 (°)")
    for idx, (x, y, z) in enumerate(foot_trajectory()):
        th1, th2, th3 = inverse_kinematics(x, y, z)
        # Convert radians to degrees for readability
        # print(
        #     f"{idx:3d}\t{np.degrees(th1):6.2f}\t{np.degrees(th2):6.2f}\t{np.degrees(th3):6.2f}"
        # )
