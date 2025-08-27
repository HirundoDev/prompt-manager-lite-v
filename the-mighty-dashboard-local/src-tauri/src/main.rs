// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::process::Command;
use std::path::PathBuf;
use serde::{Deserialize, Serialize};
use tauri::{command, State};

#[derive(Debug, Serialize, Deserialize)]
struct ProjectInfo {
    id: String,
    name: String,
    organization: String,
    path: String,
    exists: bool,
    created_at: String,
    description: Option<String>,
    tags: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct CommandResult {
    success: bool,
    output: String,
    error: Option<String>,
}

// Comando para ejecutar scripts de mighty-task
#[command]
async fn execute_mighty_task_command(args: Vec<String>) -> Result<CommandResult, String> {
    let script_path = "../the-mighty-task-template/scripts/mighty-task.py";
    
    let mut cmd = Command::new("python3");
    cmd.arg(script_path);
    
    for arg in args {
        cmd.arg(arg);
    }
    
    match cmd.output() {
        Ok(output) => {
            let stdout = String::from_utf8_lossy(&output.stdout).to_string();
            let stderr = String::from_utf8_lossy(&output.stderr).to_string();
            
            Ok(CommandResult {
                success: output.status.success(),
                output: stdout,
                error: if stderr.is_empty() { None } else { Some(stderr) },
            })
        }
        Err(e) => Err(format!("Error ejecutando comando: {}", e)),
    }
}

// Comando para listar proyectos
#[command]
async fn list_projects() -> Result<Vec<ProjectInfo>, String> {
    let result = execute_mighty_task_command(vec!["project".to_string(), "list".to_string()]).await?;
    
    if result.success {
        // Aquí se parsearia la salida del comando para extraer la información de proyectos
        // Por simplicidad, devolvemos datos mock por ahora
        Ok(vec![
            ProjectInfo {
                id: "TESTORG-DEMOAPIPROJECT-20250826200936".to_string(),
                name: "Demo API Project".to_string(),
                organization: "TestOrg".to_string(),
                path: "/home/hirundodev/development/prompt-manager-lite-v/the-mighty-task-template/mighty-task-demo-api-project".to_string(),
                exists: true,
                created_at: "2025-08-26T20:09:36".to_string(),
                description: Some("Proyecto de demostración para testing de arquitectura dual".to_string()),
                tags: vec!["demo".to_string(), "api".to_string()],
            }
        ])
    } else {
        Err(format!("Error listando proyectos: {}", result.error.unwrap_or_default()))
    }
}

// Comando para obtener información del proyecto actual
#[command]
async fn get_current_project() -> Result<Option<ProjectInfo>, String> {
    let result = execute_mighty_task_command(vec!["info".to_string()]).await?;
    
    if result.success {
        // Parsear la salida para extraer información del proyecto actual
        // Por simplicidad, devolvemos datos mock por ahora
        Ok(Some(ProjectInfo {
            id: "TESTORG-DEMOAPIPROJECT-20250826200936".to_string(),
            name: "Demo API Project".to_string(),
            organization: "TestOrg".to_string(),
            path: "/home/hirundodev/development/prompt-manager-lite-v/the-mighty-task-template/mighty-task-demo-api-project".to_string(),
            exists: true,
            created_at: "2025-08-26T20:09:36".to_string(),
            description: Some("Proyecto de demostración para testing de arquitectura dual".to_string()),
            tags: vec!["demo".to_string(), "api".to_string()],
        }))
    } else {
        Ok(None)
    }
}

// Comando para crear nueva sesión
#[command]
async fn create_session(theme: String, template: Option<String>) -> Result<CommandResult, String> {
    let mut args = vec!["generate".to_string(), "--theme".to_string(), theme];
    
    if let Some(t) = template {
        args.push("--template".to_string());
        args.push(t);
    }
    
    execute_mighty_task_command(args).await
}

// Comando para consolidar misiones
#[command]
async fn consolidate_missions(output: String, theme: Option<String>) -> Result<CommandResult, String> {
    let mut args = vec!["resume".to_string(), "--output".to_string(), output];
    
    if let Some(t) = theme {
        args.push("--theme".to_string());
        args.push(t);
    }
    
    execute_mighty_task_command(args).await
}

// Comando para exportar proyecto
#[command]
async fn export_project(project_id: Option<String>, output_path: Option<String>) -> Result<CommandResult, String> {
    let mut args = vec!["project".to_string(), "export".to_string()];
    
    if let Some(id) = project_id {
        args.push("--project-id".to_string());
        args.push(id);
    }
    
    if let Some(path) = output_path {
        args.push("--output".to_string());
        args.push(path);
    }
    
    execute_mighty_task_command(args).await
}

// Comando para importar proyecto
#[command]
async fn import_project(mtp_file: String, target_path: Option<String>) -> Result<CommandResult, String> {
    let mut args = vec!["project".to_string(), "import".to_string(), mtp_file];
    
    if let Some(path) = target_path {
        args.push("--target-path".to_string());
        args.push(path);
    }
    
    execute_mighty_task_command(args).await
}

// Comando para cambiar proyecto activo
#[command]
async fn switch_project(project_id: String) -> Result<CommandResult, String> {
    execute_mighty_task_command(vec!["project".to_string(), "switch".to_string(), project_id]).await
}

// Comando para obtener estadísticas del dashboard
#[command]
async fn get_dashboard_stats() -> Result<serde_json::Value, String> {
    let result = execute_mighty_task_command(vec!["status".to_string()]).await?;
    
    if result.success {
        // Parse básico del output de status para extraer métricas reales
        let mut total_projects = 1;
        let mut active_sessions = 0;
        let mut completed_missions = 0;
        let mut total_reports = 0;
        
        for line in result.output.lines() {
            if line.contains("Sesiones encontradas:") || line.contains("Sessions found:") {
                if let Some(num_str) = line.split(':').nth(1) {
                    if let Ok(num) = num_str.trim().parse::<u32>() {
                        active_sessions = num;
                    }
                }
            } else if line.contains("Misiones completadas:") || line.contains("Completed missions:") {
                if let Some(num_str) = line.split(':').nth(1) {
                    if let Ok(num) = num_str.trim().parse::<u32>() {
                        completed_missions = num;
                    }
                }
            } else if line.contains("Reportes generados:") || line.contains("Reports generated:") {
                if let Some(num_str) = line.split(':').nth(1) {
                    if let Ok(num) = num_str.trim().parse::<u32>() {
                        total_reports = num;
                    }
                }
            }
        }
        
        Ok(serde_json::json!({
            "total_projects": total_projects,
            "active_sessions": active_sessions,
            "completed_missions": completed_missions,
            "total_reports": total_reports,
            "last_activity": chrono::Utc::now().to_rfc3339()
        }))
    } else {
        // Fallback a datos mock si hay error
        Ok(serde_json::json!({
            "total_projects": 1,
            "active_sessions": 0,
            "completed_missions": 0,
            "total_reports": 0,
            "last_activity": chrono::Utc::now().to_rfc3339()
        }))
    }
}

// Comando para ejecutar tests del sistema
#[command]
async fn run_system_test(test_type: String) -> Result<CommandResult, String> {
    let args = vec!["../scripts/test-system.py".to_string(), format!("--{}-test", test_type)];
    
    let mut cmd = Command::new("python3");
    for arg in args {
        cmd.arg(arg);
    }
    
    match cmd.output() {
        Ok(output) => {
            let stdout = String::from_utf8_lossy(&output.stdout).to_string();
            let stderr = String::from_utf8_lossy(&output.stderr).to_string();
            
            Ok(CommandResult {
                success: output.status.success(),
                output: stdout,
                error: if stderr.is_empty() { None } else { Some(stderr) },
            })
        }
        Err(e) => Err(format!("Error ejecutando test: {}", e)),
    }
}

// Comando para crear nuevo proyecto
#[command]
async fn create_project(name: String, org: String) -> Result<CommandResult, String> {
    execute_mighty_task_command(vec![
        "project".to_string(),
        "create".to_string(),
        "--name".to_string(),
        name,
        "--org".to_string(),
        org
    ]).await
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            execute_mighty_task_command,
            list_projects,
            get_current_project,
            create_session,
            consolidate_missions,
            export_project,
            import_project,
            switch_project,
            get_dashboard_stats,
            run_system_test,
            create_project
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
