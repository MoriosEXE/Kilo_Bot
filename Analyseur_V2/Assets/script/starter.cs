using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEditor;
using UnityEngine;

public class starter : MonoBehaviour
{
    public GameObject kilo_bot;

    // Start is called before the first frame update
    void Start()
    {
        string filePath = EditorUtility.OpenFilePanel("Select File", "", "txt");
        if (filePath.Length != 0)
        {
            using (StreamReader reader = new StreamReader(filePath))
            {
                string content = reader.ReadToEnd();
                Debug.Log(content);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
