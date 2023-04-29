Sub EnviarMensajeChatGPT()

    ' Crea una instancia del navegador
    Dim objIE As Object
    Set objIE = CreateObject("InternetExplorer.Application")
    
    ' Navega a la página de ChatGPT
    objIE.navigate "https://chatgpt.com/"
    
    ' Espera a que la página se cargue completamente
    Do While objIE.Busy Or objIE.readyState <> 4
        Application.Wait DateAdd("s", 1, Now)
    Loop
    
    ' Busca el cuadro de texto y escribe el mensaje
    objIE.Document.getElementById("userInput").Value = "hola chat gpt, ¿qué hora es?"
    
    ' Presiona Enter para enviar el mensaje
    objIE.Document.getElementById("userInput").FireEvent ("onkeydown")
    
    ' Espera a que ChatGPT envíe la respuesta
    Application.Wait DateAdd("s", 5, Now)
    
    ' Lee la respuesta de ChatGPT y extrae la hora
    Dim respuesta As String
    respuesta = objIE.Document.getElementById("conversation").innerText
    
    Dim hora As String
    hora = extraerHora(respuesta)
    
    ' Muestra la hora en una ventana de mensaje
    MsgBox "La hora actual es: " & hora
    
    ' Cierra el navegador
    objIE.Quit
    Set objIE = Nothing

End Sub

Function extraerHora(respuesta As String) As String

    Dim hora As String
    
    ' Busca una cadena de texto que se parezca a una hora
    Dim horaRegex As Object
    Set horaRegex = CreateObject("VBScript.RegExp")
    horaRegex.Pattern = "\d{1,2}:\d{2}\s*[AaPp]\.?[Mm]\.?"
    horaRegex.Global = True
    
    Dim matches As Object
    Set matches = horaRegex.Execute(respuesta)
    
    ' Extrae la primera cadena de texto que coincide con el patrón
    If matches.Count > 0 Then
        hora = matches.Item(0)
    Else
        hora = "No se pudo extraer la hora"
    End If
    
    extraerHora = hora
    
End Function