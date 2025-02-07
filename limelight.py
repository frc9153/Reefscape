from ntcore import NetworkTableInstance

def get_target_pose_in_camera_space():
    return NetworkTableInstance.getDefault().getTable("limelight").getEntry("targetpose_cameraspace").getDoubleArray([0, 0, 0, 0, 0, 0])
