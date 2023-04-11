using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class kilo_bot : MonoBehaviour
{
    public int id { get; set; }
    public int step { get; set; }

    private int opinion;
    public int Opinion { 
        get { return opinion; }
        set
        {
            opinion = value;
            // Trouver l'objet "pyramid" dans la scène
            GameObject pyramid = transform.Find("pyramid").gameObject;
          
            if (pyramid.GetComponent<MeshRenderer>() != null)
            {
                if (opinion == 11)
                {
                    // Changer la couleur de l'objet
                    pyramid.GetComponent<MeshRenderer>().material.color = Color.red;
                }
                else
                {
                    pyramid.GetComponent<MeshRenderer>().material.color = Color.green;
                }

            }
            
        }
    }
    public int puissance { get; set; }


    private bool is_visible; 
    public bool Is_visible
    { 
        get { return  is_visible; }
        set 
        { 
            is_visible = value;
            // Récupérer tous les composants Renderer des sous-objets de l'objet principal
            Renderer[] renderers = GetComponentsInChildren<Renderer>();

            // Désactiver tous les composants Renderer des sous-objets
            foreach (Renderer renderer in renderers)
            {
                renderer.enabled = is_visible;
            }
        } 
    }

    // Start is called before the first frame update
    void Start()
    {


    }

    // Update is called once per frame
    void Update()
    {


    }




}
