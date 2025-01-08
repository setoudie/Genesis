print("Hello Genesis")

import genesis as gs

# Initialisation avec le backend GPU
gs.init(backend=gs.cpu)

# Création de la scène avec le visualiseur
scene = gs.Scene(show_viewer=False)

# Ajout des entités à la scène
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)

# Creation d'une camera
cam = scene.add_camera(
    res    = (640, 480),
    pos    = (3.5, 0.0, 2.5),
    lookat = (0, 0, 0.5),
    fov    = 30,
    GUI    = False,
)

# Construction de la scène
scene.build()

# Debut enregistrement
cam.start_recording()
import numpy as np

# Boucle de simulation
for i in range(1000):
    scene.step()
    cam.set_pose(
        pos    = (3.0 * np.sin(i / 60), 3.0 * np.cos(i / 60), 2.5),
        lookat = (0, 0, 0.5),
    )
    cam.render()
cam.stop_recording(save_to_filename='hello_gs_video.mp4', fps=60)