using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Text.RegularExpressions;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.UIElements;
using UnityEngine.Windows;

public class starter : MonoBehaviour
{
    public GameObject kilo_bot;
    public List<List<List<object>>> data;
    public List<Dictionary<int,GameObject>> instance_kilobot;
    public InputField step_filed;
    public InputField id_field;

    // Start is called before the first frame update
    void Start()
    {
        step_filed = GetComponentInChildren<InputField>();
    }




    public void generate_log()
    {
        foreach(var step in data)
        {
            foreach(var bot in step)
            {
                //Dictionary<int, GameObject> dict = new Dictionary<int, GameObject>();
                
                Vector3 position = new Vector3((float)bot[1] * 10, 0, (float)bot[2] * 10); // Position d'instanciation
                Quaternion rotation = Quaternion.Euler(0f,(float) bot[3], 0f); // Créer une rotation à partir de l'angle Y
                Instantiate(kilo_bot, position, rotation); // Instancier l'objet avec la position et la rotation
                //dict.Add((int)bot[0],Instantiate(kilo_bot,new Vector3((float) bot[1], (float)bot[2],0),Quaternion.identity));
                //instance_kilobot.Add(dict);
            }
        }
    } 

    public void Open_File()
    {
        string filePath = EditorUtility.OpenFilePanel("Select File", "", "txt");
        if (filePath.Length != 0)
        {
            using (StreamReader reader = new StreamReader(filePath))
            {    
                String content = reader.ReadToEnd();
      
                data = DataRead(content);
                generate_log();
            }
        }
    }

    public static List<List<List<object>>> DataRead(string name, bool typeData = true)
    {
        List<List<List<object>>> dataByTime = new List<List<List<object>>>();
        List<List<List<object>>> dataByRobot = new List<List<List<object>>>();

    
        {
            string rawLine = name;
            string[] rawLines = rawLine.Split("step");

            foreach (string rawData in rawLines)
            {
                if (rawData != "")
                {
                    string[] brutLine = rawData.Split("\n");

                    string step = brutLine[0];
                    List<List<object>> stepDt = new List<List<object>>();

                    foreach (string bot in brutLine)
                    {
                        if (bot.Contains("ID"))
                        {
                            int idBot = int.Parse(bot.Split("=")[1].Split(" ")[1]);
                            float posX = float.Parse(bot.Split("=")[2].Split(" ")[1], CultureInfo.InvariantCulture.NumberFormat);
                            float posY = float.Parse(bot.Split("=")[3].Split(" ")[1], CultureInfo.InvariantCulture.NumberFormat);
                            float angle = float.Parse(bot.Split("=")[4].Split(" ")[1], CultureInfo.InvariantCulture.NumberFormat);
                            int opinion = int.Parse( bot.Split("=")[5].Split(" ")[1]);
                            stepDt.Add(new List<object> { idBot, posX, posY ,angle,opinion});
                        }
                    }

                    dataByTime.Add(stepDt);
                }
            }
        }

        if (typeData)
        {
            return dataByTime;
        }
        else
        {
            return dataByRobot;
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
