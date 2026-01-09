#r "nuget: Newtonsoft.Json, 13.0.3"

using System;
using System.IO;
using Newtonsoft.Json.Linq;
using System;
using System.IO;
using Newtonsoft.Json.Linq;

class TelemetryParser
{
    static void Main()
    {
        string jsonFile = "sample_telemetry.json";
        var jsonData = File.ReadAllText(jsonFile);
        var jObject = JObject.Parse(jsonData);

        foreach (var proc in jObject["DeviceProcessEvents"])
        {
            Console.WriteLine($"Process: {proc["ProcessName"]}, CommandLine: {proc["ProcessCommandLine"]}");
        }
    }
}
