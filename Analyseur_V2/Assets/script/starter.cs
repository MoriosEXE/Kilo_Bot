using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
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
    public List<Dictionary<int,GameObject>> instance_kilobot = new List<Dictionary<int,GameObject>>();
    Dictionary<int, GameObject> dict_bot = new Dictionary<int, GameObject>();

    private List<int> step_list = new List<int>();
    private List<int> id_list = new List<int>();

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

    }



    public void read_step(string s)
    {
        step_list.Clear();
        step_list = ParseNumbers(s);
        foreach (int i in step_list) { print(i); }
    }
    public void read_id(string s)
    {
        id_list.Clear();
        id_list= ParseNumbers(s);
    }



    public void generate_log()
    {
        foreach(var step in data)
        {

            dict_bot.Clear();
            foreach (var bot in step)
            {

                Vector3 position = new Vector3((float)bot[1] * 10, 0, (float)bot[2] * 10); // Position d'instanciation
                Quaternion rotation = Quaternion.Euler(0f,(float) bot[3], 0f); // Créer une rotation à partir de l'angle Y
                GameObject temp_bot = Instantiate(kilo_bot , position, rotation); // Instancier l'objet avec la position et la rotation
                //temp_bot.GetComponent<GameObject>().id = bot[0];
                dict_bot.Add((int)bot[0], temp_bot);

            }
            
            instance_kilobot.Add(dict_bot);
            
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



    static List<int> ParseNumbers(string input)
    {
        List<int> numbers = new List<int>();
        foreach (string group in input.Split(','))
        {
            if (Regex.IsMatch(group, @"^\d+$"))
            {
                // Add single number
                numbers.Add(int.Parse(group));
            }
            else if (Regex.IsMatch(group, @"^\d+-\d+$"))
            {
                // Add range of numbers
                Match match = Regex.Match(group, @"(\d+)-(\d+)"); 
                int start = int.Parse(match.Groups[1].Value);
                int end = int.Parse(match.Groups[2].Value);
                for (int i = start; i <= end; i++)
                {
                    numbers.Add(i);
                }
            }
            else
            {
                throw new ArgumentException("Invalid input format");
            }
        }
        // Sort and remove duplicates
        return numbers.OrderBy(n => n).Distinct().ToList();
    }
}
