from fastapi import FastAPI, Depends
import uvicorn
from contextlib import asynccontextmanager
import logging

from app.core.util.id_manager import get_unique_id_instance
from app.core.db.database import db
from app.features.student.presentation.routes.students_routers import student_router
from app.features.teacher.presentation.routes.teachers_routers import teacher_router
from app.features.classroom.presentation.routes.classrooms_routers import classroom_router
from app.features.course.presentation.routes.courses_routers import course_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with db.engine.begin() as conn:
            await conn.run_sync(db.Base.metadata.create_all)
        
        print("Start the app")
        print("Registered routes:")
        for route in app.routes:
            print(route.path)
        
        app.state.unique_id = await get_unique_id_instance()
        try:
            app.state.unique_id.load_from_file('unique_id_state.json')
        except Exception as e:
            print(f"Error loading unique_id_state.json: {e}")
            raise
        
        yield
    
    except Exception as e:
        print(f"Error during app startup: {e}")
        raise
    
    finally:
        try:
            if app.state.unique_id:
                app.state.unique_id.save_to_file('unique_id_state.json')
        except Exception as e:
            print(f"Error saving unique_id_state.json: {e}")

app = FastAPI(lifespan=lifespan)

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(classroom_router)
app.include_router(course_router)
#app.include_router(athentication.router)
 
@app.get('/')
def start():
    return 'this is my university project!!'
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
