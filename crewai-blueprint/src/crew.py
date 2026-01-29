from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from src.tools.custom_tool import EnterpriseSearchTool

@CrewBase
class BlueprintCrew():
	"""Blueprint crew"""
	agents_config = '../config/agents.yaml'
	tasks_config = '../config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[EnterpriseSearchTool()], # Custom enterprise tool
			verbose=True
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Blueprint crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # For more complex tasks
		)
