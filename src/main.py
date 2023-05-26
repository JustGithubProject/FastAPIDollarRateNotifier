from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from src.em import send_email_report_dashboard


app = FastAPI(
    title="Service"
)

templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})


@app.post("/process_form")
async def process_form(request: Request, background_tasks: BackgroundTasks):
    form_data = await request.form()
    email_data = str(form_data["email"])
    if "@gmail.com" not in email_data:
        error_message = "Invalid email"
        return templates.TemplateResponse("response.html", {"request": request, "error_message": error_message})
    background_tasks.add_task(send_email_report_dashboard, email_data)
    success_message = "Email was sent successfully"
    return templates.TemplateResponse("response_2.html", {"request": request, "success_message": success_message})
