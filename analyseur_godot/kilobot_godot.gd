extends Node3D


# Called when the node enters the scene tree for the first time.
func _ready():
	var my_mesh_instance = get_node("pyramid")

	# Créez un nouveau matériau avec la nouvelle couleur
	var new_material = StandardMaterial3D.new()
	new_material.albedo_color = Color(1, 0, 0, 1) # rouge opaque
	#new_material.albedo_color = Color(0, 1, 0, 1) # vert opaque
# Appliquez le nouveau matériau au MeshInstance
	my_mesh_instance.material_override = new_material
	
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

