<script>
	import { onMount } from 'svelte';
	import Header from '$lib/components/Header.svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
	import ProjectCreator from '$lib/components/ProjectCreator.svelte';
	import SessionCreator from '$lib/components/SessionCreator.svelte';
	import TestRunner from '$lib/components/TestRunner.svelte';
	import { Play, Users, CheckCircle, FolderOpen, Plus, TestTube, Home, FileText, BarChart3, Settings } from 'lucide-svelte';
	import { invoke } from '$lib/utils/tauri.js';
	import { showNotification } from '$lib/utils/notifications.js';
	import HelpIcon from '$lib/components/HelpIcon.svelte';
	import HelpTooltip from '$lib/components/HelpTooltip.svelte';
	import { getContext } from 'svelte';
	
	// Contexto de ayuda
	const help = getContext('help');
	
	// Estado del dashboard
	let stats = {
		totalProjects: 0,
		activeProject: null,
		recentSessions: 0,
		completedMissions: 0
	};
	
	let recentActivity = [];
	
	// Referencias a los modales
	let projectCreator;
	let sessionCreator;
	let testRunner;
	
	// Acciones rápidas disponibles
	const quickActions = [
		{
			title: 'Nueva Sesión',
			description: 'Crear sesión de trabajo',
			icon: Plus,
			action: 'create-session',
			color: 'primary',
			helpKey: 'dashboard.actions.new-session'
		},
		{
			title: 'Ejecutar Tests',
			description: 'Correr tests del sistema',
			icon: Play,
			action: 'run-tests',
			color: 'success',
			helpKey: 'dashboard.actions.run-tests'
		},
		{
			title: 'Reportes',
			description: 'Ver estadísticas y métricas',
			icon: BarChart3,
			action: 'view-reports',
			color: 'warning',
			helpKey: 'dashboard.actions.view-reports'
		}
	];
	
	let dashboardStats = {
		total_projects: 0,
		active_sessions: 0,
		completed_missions: 0,
		total_reports: 0
	};

	let currentProject = null;
	let isLoading = true;

	onMount(async () => {
		try {
			// Cargar estadísticas del dashboard
			dashboardStats = await invoke('get_dashboard_stats');
			
			// Cargar proyecto actual
			currentProject = await invoke('get_current_project');
			
			stats = {
				totalProjects: dashboardStats.total_projects || 0,
				activeProject: currentProject || null,
				recentSessions: dashboardStats.active_sessions || 0,
				completedMissions: dashboardStats.completed_missions || 0
			};
			
			isLoading = false;
		} catch (error) {
			console.error('Error loading dashboard data:', error);
			isLoading = false;
		}
	});
	
	async function loadRecentActivity() {
		try {
			// Simular actividad reciente
			recentActivity = [
				{
					type: 'session',
					title: 'Sesión BACKEND-API-SETUP creada',
					timestamp: '2025-08-26 19:30',
					status: 'success'
				},
				{
					type: 'mission',
					title: 'Misión API-DEVELOPMENT consolidada',
					timestamp: '2025-08-26 18:45',
					status: 'success'
				},
				{
					type: 'project',
					title: 'Proyecto Demo API Project creado',
					timestamp: '2025-08-26 18:00',
					status: 'info'
				}
			];
		} catch (error) {
			console.error('Error cargando actividad reciente:', error);
		}
	}
	
	function handleQuickAction(action) {
		switch (action) {
			case 'create-session':
				sessionCreator?.open();
				break;
			case 'run-tests':
				testRunner?.open();
				break;
			case 'view-reports':
				window.location.href = '/reports';
				break;
		}
	}
	
	function handleProjectCreated(event) {
		console.log('Proyecto creado:', event.detail);
		loadDashboardData();
	}
	
	function handleSessionCreated(event) {
		console.log('Sesión creada:', event.detail);
		loadDashboardData();
	}
	
	async function loadDashboardData() {
		try {
			dashboardStats = await invoke('get_dashboard_stats');
			currentProject = await invoke('get_current_project');
			
			stats = {
				totalProjects: dashboardStats.total_projects || 0,
				activeProject: currentProject || null,
				recentSessions: dashboardStats.active_sessions || 0,
				completedMissions: dashboardStats.completed_missions || 0
			};
		} catch (error) {
			console.error('Error loading dashboard data:', error);
		}
	}
	
	function getStatusColor(status) {
		const colors = {
			success: 'text-success-600 bg-success-100',
			info: 'text-primary-600 bg-primary-100',
			warning: 'text-warning-600 bg-warning-100',
			error: 'text-error-600 bg-error-100'
		};
		return colors[status] || colors.info;
	}
	
	function getActionColor(color) {
		const colors = {
			primary: 'bg-primary-500 hover:bg-primary-600',
			success: 'bg-success-500 hover:bg-success-600',
			secondary: 'bg-secondary-500 hover:bg-secondary-600',
			warning: 'bg-warning-500 hover:bg-warning-600'
		};
		return colors[color] || colors.primary;
	}
</script>

<svelte:head>
	<title>Dashboard - The Mighty Task</title>
</svelte:head>

<div class="space-y-6">
	<!-- Header del Dashboard -->
	<div class="mighty-fade-in">
		<h1 class="text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
			<Home class="w-8 h-8 text-primary-600" />
			Dashboard Local
		</h1>
		<p class="mt-2 text-gray-600 dark:text-gray-400">
			Gestión local de proyectos mighty-task con acceso directo al filesystem
		</p>
	</div>
	
	<!-- Estadísticas principales -->
	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mighty-slide-up">
		<div class="mighty-card">
			<div class="flex items-center justify-between">
				<div class="flex items-center">
					<div class="flex-shrink-0">
						<FolderOpen class="w-8 h-8 text-primary-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-500 dark:text-gray-400">Proyectos Totales</p>
						<p class="text-2xl font-semibold text-gray-900 dark:text-white">{stats.totalProjects}</p>
					</div>
				</div>
				<HelpTooltip text={help.getTooltipText('dashboard.stats.projects')}>
					<HelpIcon helpKey="dashboard.stats.projects" variant="modal" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
		
		<div class="mighty-card">
			<div class="flex items-center justify-between">
				<div class="flex items-center">
					<div class="flex-shrink-0">
						<FileText class="w-8 h-8 text-success-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-500 dark:text-gray-400">Sesiones Recientes</p>
						<p class="text-2xl font-semibold text-gray-900 dark:text-white">{stats.recentSessions}</p>
					</div>
				</div>
				<HelpTooltip text={help.getTooltipText('dashboard.stats.sessions')}>
					<HelpIcon helpKey="dashboard.stats.sessions" variant="modal" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
		
		<div class="mighty-card">
			<div class="flex items-center justify-between">
				<div class="flex items-center">
					<div class="flex-shrink-0">
						<BarChart3 class="w-8 h-8 text-warning-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-500 dark:text-gray-400">Misiones Completadas</p>
						<p class="text-2xl font-semibold text-gray-900 dark:text-white">{stats.completedMissions}</p>
					</div>
				</div>
				<HelpTooltip text={help.getTooltipText('dashboard.stats.missions')}>
					<HelpIcon helpKey="dashboard.stats.missions" variant="modal" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
		
		<div class="mighty-card">
			<div class="flex items-center justify-between">
				<div class="flex items-center">
					<div class="flex-shrink-0">
						<Settings class="w-8 h-8 text-secondary-600" />
					</div>
					<div class="ml-4">
						<p class="text-sm font-medium text-gray-500 dark:text-gray-400">Proyecto Activo</p>
						<p class="text-lg font-semibold text-gray-900 dark:text-white truncate">
							{stats.activeProject || 'Ninguno'}
						</p>
					</div>
				</div>
				<HelpTooltip text={help.getTooltipText('projects.status.active')}>
					<HelpIcon helpKey="projects.status.active" variant="modal" on:help={(e) => help.showModal(e.detail.helpKey)} />
				</HelpTooltip>
			</div>
		</div>
	</div>
	
	<!-- Acciones rápidas -->
	<div class="mighty-slide-up" style="animation-delay: 0.1s;">
		<h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">Acciones Rápidas</h2>
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
			{#each quickActions as action}
				<div class="mighty-card hover:shadow-md mighty-transition relative">
					<button
						class="w-full text-left"
						on:click={() => handleQuickAction(action.action)}
					>
						<div class="flex items-start space-x-3">
							<div class="flex-shrink-0">
								<div class="w-10 h-10 rounded-lg {getActionColor(action.color)} flex items-center justify-center">
									<svelte:component this={action.icon} class="w-5 h-5 text-white" />
								</div>
							</div>
							<div class="flex-1 min-w-0">
								<h3 class="text-sm font-medium text-gray-900 dark:text-white">
									{action.title}
								</h3>
								<p class="text-sm text-gray-500 dark:text-gray-400 mt-1">
									{action.description}
								</p>
							</div>
						</div>
					</button>
					<div class="absolute top-2 right-2">
						<HelpTooltip text={help.getTooltipText(action.helpKey)}>
							<HelpIcon helpKey={action.helpKey} variant="modal" size="sm" on:help={(e) => help.showModal(e.detail.helpKey)} />
						</HelpTooltip>
					</div>
				</div>
			{/each}
		</div>
	</div>
	
	<!-- Actividad reciente -->
	<div class="mighty-slide-up" style="animation-delay: 0.2s;">
		<h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">Actividad Reciente</h2>
		<div class="mighty-card">
			{#if recentActivity.length > 0}
				<div class="space-y-4">
					{#each recentActivity as activity}
						<div class="flex items-center space-x-3">
							<div class="flex-shrink-0">
								<div class="w-2 h-2 rounded-full {getStatusColor(activity.status)}"></div>
							</div>
							<div class="flex-1 min-w-0">
								<p class="text-sm font-medium text-gray-900 dark:text-white">
									{activity.title}
								</p>
								<p class="text-sm text-gray-500 dark:text-gray-400">
									{activity.timestamp}
								</p>
							</div>
							<div class="flex-shrink-0">
								<span class="mighty-badge {getStatusColor(activity.status)}">
									{activity.type}
								</span>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<div class="text-center py-8">
					<FileText class="w-12 h-12 text-gray-400 mx-auto mb-4" />
					<p class="text-gray-500 dark:text-gray-400">No hay actividad reciente</p>
				</div>
			{/if}
		</div>
	</div>
	
	<!-- Modales -->
	<ProjectCreator bind:this={projectCreator} on:projectCreated={handleProjectCreated} />
	<SessionCreator bind:this={sessionCreator} on:sessionCreated={handleSessionCreated} />
	<TestRunner bind:this={testRunner} />
	
	<!-- Información del sistema -->
	<div class="mighty-slide-up" style="animation-delay: 0.3s;">
		<div class="mighty-card bg-gradient-to-r from-primary-50 to-secondary-50 dark:from-primary-900/20 dark:to-secondary-900/20">
			<div class="flex items-center space-x-4">
				<div class="flex-shrink-0">
					<div class="w-12 h-12 bg-primary-600 rounded-lg flex items-center justify-center">
						<Home class="w-6 h-6 text-white" />
					</div>
				</div>
				<div class="flex-1">
					<h3 class="text-lg font-semibold text-gray-900 dark:text-white">
						The Mighty Task - Dashboard Local
					</h3>
					<p class="text-gray-600 dark:text-gray-400">
						Versión 1.0.0 • Svelte 5 + Tauri • Acceso directo al filesystem
					</p>
				</div>
				<div class="flex-shrink-0">
					<span class="mighty-badge-success">Local</span>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	/* Animaciones escalonadas */
	.mighty-slide-up:nth-child(2) { animation-delay: 0.1s; }
	.mighty-slide-up:nth-child(3) { animation-delay: 0.2s; }
	.mighty-slide-up:nth-child(4) { animation-delay: 0.3s; }
</style>
