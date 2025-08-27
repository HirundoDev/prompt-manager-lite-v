use std::process::Command;
use std::path::Path;
use serde::{Deserialize, Serialize};
use tauri::command;

#[derive(Debug, Serialize, Deserialize)]
pub struct CommandResult {
    pub success: bool,
    pub message: String,
    pub data: Option<serde_json::Value>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct Project {
    pub id: String,
    pub name: String,
    pub org: String,
    pub created_at: String,
    pub path: String,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct DashboardStats {
    pub total_projects: u32,
    pub active_sessions: u32,
    pub completed_missions: u32,
    pub total_reports: u32,
}

// Ruta base del sistema mighty-task
const MIGHTY_TASK_BASE: &str = "/home/hirundodev/development/prompt-manager-lite-v/the-mighty-task-template";

#[command]
pub async fn list_projects() -> Result<Vec<Project>, String> {
    let output = Command::new("python3")
        .arg("scripts/mighty-task.py")
        .arg("project")
        .arg("list")
        .arg("--format")
        .arg("json")
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    if !output.status.success() {
        return Err(format!("Error en mighty-task: {}", String::from_utf8_lossy(&output.stderr)));
    }

    let output_str = String::from_utf8_lossy(&output.stdout);
    
    // Parse del output JSON
    match serde_json::from_str::<Vec<Project>>(&output_str) {
        Ok(projects) => Ok(projects),
        Err(_) => {
            // Fallback: parsear output de texto plano
            let mut projects = Vec::new();
            for line in output_str.lines() {
                if line.contains("ID:") {
                    // Parsear línea de proyecto
                    if let Some(id_start) = line.find("ID: ") {
                        let id_part = &line[id_start + 4..];
                        if let Some(id_end) = id_part.find(" ") {
                            let id = id_part[..id_end].to_string();
                            projects.push(Project {
                                id: id.clone(),
                                name: "Proyecto".to_string(),
                                org: "Org".to_string(),
                                created_at: "2025-01-01".to_string(),
                                path: format!("{}/projects/{}", MIGHTY_TASK_BASE, id),
                            });
                        }
                    }
                }
            }
            Ok(projects)
        }
    }
}

#[command]
pub async fn get_current_project() -> Result<Option<Project>, String> {
    let current_project_file = format!("{}/.current_project", MIGHTY_TASK_BASE);
    
    if let Ok(content) = std::fs::read_to_string(&current_project_file) {
        let project_id = content.trim();
        if !project_id.is_empty() {
            return Ok(Some(Project {
                id: project_id.to_string(),
                name: "Proyecto Actual".to_string(),
                org: "Org".to_string(),
                created_at: "2025-01-01".to_string(),
                path: format!("{}/projects/{}", MIGHTY_TASK_BASE, project_id),
            }));
        }
    }
    
    Ok(None)
}

#[command]
pub async fn switch_project(project_id: String) -> Result<CommandResult, String> {
    let output = Command::new("python3")
        .arg("scripts/mighty-task.py")
        .arg("project")
        .arg("switch")
        .arg(&project_id)
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output.status.success();
    let message = if success {
        format!("Proyecto {} activado exitosamente", project_id)
    } else {
        format!("Error cambiando proyecto: {}", String::from_utf8_lossy(&output.stderr))
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn create_project(name: String, org: String) -> Result<CommandResult, String> {
    let output = Command::new("python3")
        .arg("scripts/mighty-task.py")
        .arg("project")
        .arg("create")
        .arg("--name")
        .arg(&name)
        .arg("--org")
        .arg(&org)
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output.status.success();
    let message = if success {
        format!("Proyecto {} creado exitosamente", name)
    } else {
        format!("Error creando proyecto: {}", String::from_utf8_lossy(&output.stderr))
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn export_project(project_id: Option<String>, output_path: String) -> Result<CommandResult, String> {
    let mut cmd = Command::new("python3");
    cmd.arg("scripts/mighty-task.py")
       .arg("project")
       .arg("export")
       .arg("--output")
       .arg(&output_path);
    
    if let Some(id) = project_id {
        cmd.arg("--project-id").arg(&id);
    }
    
    let output = cmd.current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output.status.success();
    let message = if success {
        format!("Proyecto exportado a {}", output_path)
    } else {
        format!("Error exportando proyecto: {}", String::from_utf8_lossy(&output.stderr))
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn import_project(mtp_file: String) -> Result<CommandResult, String> {
    let output = Command::new("python3")
        .arg("scripts/mighty-task.py")
        .arg("project")
        .arg("import")
        .arg(&mtp_file)
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output.status.success();
    let message = if success {
        format!("Proyecto importado desde {}", mtp_file)
    } else {
        format!("Error importando proyecto: {}", String::from_utf8_lossy(&output.stderr))
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn create_session(theme: String, template: String) -> Result<CommandResult, String> {
    let output = Command::new("python3")
        .arg("scripts/mighty-task.py")
        .arg("generate")
        .arg("--theme")
        .arg(&theme)
        .arg("--template")
        .arg(&template)
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output.status.success();
    let message = if success {
        format!("Sesión {} creada exitosamente", theme)
    } else {
        format!("Error creando sesión: {}", String::from_utf8_lossy(&output.stderr))
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn consolidate_missions(output: String, theme: Option<String>) -> Result<CommandResult, String> {
    let mut cmd = Command::new("python3");
    cmd.arg("scripts/mighty-task.py")
       .arg("resume")
       .arg("--output")
       .arg(&output);
    
    if let Some(t) = theme {
        cmd.arg("--theme").arg(&t);
    }
    
    let output_result = cmd.current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output_result.status.success();
    let message = if success {
        format!("Misiones consolidadas en {}", output)
    } else {
        format!("Error consolidando misiones: {}", String::from_utf8_lossy(&output_result.stderr))
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn get_dashboard_stats() -> Result<DashboardStats, String> {
    let output = Command::new("python3")
        .arg("scripts/mighty-task.py")
        .arg("status")
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    if !output.status.success() {
        return Err(format!("Error obteniendo estadísticas: {}", String::from_utf8_lossy(&output.stderr)));
    }

    let output_str = String::from_utf8_lossy(&output.stdout);
    
    // Parse básico del output de status
    let mut stats = DashboardStats {
        total_projects: 1,
        active_sessions: 0,
        completed_missions: 0,
        total_reports: 0,
    };
    
    for line in output_str.lines() {
        if line.contains("Sesiones encontradas:") {
            if let Some(num_str) = line.split(':').nth(1) {
                if let Ok(num) = num_str.trim().parse::<u32>() {
                    stats.active_sessions = num;
                }
            }
        } else if line.contains("Misiones completadas:") {
            if let Some(num_str) = line.split(':').nth(1) {
                if let Ok(num) = num_str.trim().parse::<u32>() {
                    stats.completed_missions = num;
                }
            }
        } else if line.contains("Reportes generados:") {
            if let Some(num_str) = line.split(':').nth(1) {
                if let Ok(num) = num_str.trim().parse::<u32>() {
                    stats.total_reports = num;
                }
            }
        }
    }
    
    Ok(stats)
}

#[command]
pub async fn execute_mighty_task_command(args: Vec<String>) -> Result<CommandResult, String> {
    let mut cmd = Command::new("python3");
    cmd.arg("scripts/mighty-task.py");
    
    for arg in args {
        cmd.arg(arg);
    }
    
    let output = cmd.current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando comando: {}", e))?;

    let success = output.status.success();
    let stdout = String::from_utf8_lossy(&output.stdout);
    let stderr = String::from_utf8_lossy(&output.stderr);
    
    let message = if success {
        stdout.to_string()
    } else {
        format!("Error: {}", stderr)
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}

#[command]
pub async fn run_system_test(test_type: String) -> Result<CommandResult, String> {
    let output = Command::new("python3")
        .arg("scripts/test-system.py")
        .arg(format!("--{}-test", test_type))
        .current_dir(MIGHTY_TASK_BASE)
        .output()
        .map_err(|e| format!("Error ejecutando test: {}", e))?;

    let success = output.status.success();
    let stdout = String::from_utf8_lossy(&output.stdout);
    let stderr = String::from_utf8_lossy(&output.stderr);
    
    let message = if success {
        format!("Test {} completado:\n{}", test_type, stdout)
    } else {
        format!("Error en test {}: {}", test_type, stderr)
    };

    Ok(CommandResult {
        success,
        message,
        data: None,
    })
}
